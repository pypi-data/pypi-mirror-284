import logging
import re
import os
from PySide6.QtCore import QObject, Signal, QDir
from PySide6.QtWidgets import QApplication
from pdfp.settings_window import SettingsWindow
from pdfp.utils.filename_constructor import construct_filename
from pdfp.utils.clean_text import clean_text
from pdfp.utils.tts_limit import tts_word_count
from gtts import gTTS
import pymupdf

class SharedState:
    """
    Stores shared state information for text-to-speech (TTS) conversion progress tracking.
    Attributes:
        progress (int): Current progress of the operation.
        total_parts (int): Total parts of the operation.
        progress_percentage (float): Percentage of completion of the operation.
    """
    def __init__(self):
        self.progress = 0
        self.total_parts = 0 
        self.progress_percentage = 0

class QueueHandler(logging.Handler):
    """
    Custom logging handler for processing specific log messages during TTS conversion.

    Args:
        shared_state (SharedState): Shared state object for tracking conversion progress.
        op_msgs (Signal): Signal to emit operation messages. Connects to progress_widget.
        worker_progress (Signal): Signal to update the progress bar. Connects to progress_widget.
        revise_worker_label (Signal): Signal to revise the progress bar label. Connects to progress_widget.
        worker_name (str): Name of the worker for logging purposes.
    """
    def __init__(self, shared_state, op_msgs, worker_progress, revise_worker_label, worker_name):
        super().__init__()
        self.shared_state = shared_state
        self.op_msgs = op_msgs
        self.worker_progress = worker_progress
        self.revise_worker_label = revise_worker_label
        self.worker_name = worker_name
    
    def emit(self, record):
        """
        Emit the log record to process specific messages and update UI elements.
        Args:
            record (LogRecord): The log record to process.
        Notes:
            - Updates total_parts based on specific log messages.
            - Updates progress and progress percentage when a part is created.
        """
        try:
            msg = self.format(record)
            
            match = re.search(r"text_parts: (\d+)", msg)
            if match:
                digit_str = match.group(1)
                self.shared_state.total_parts = int(digit_str)
                QApplication.processEvents()
            
            match = re.search(r"part-(\d+) created", msg)
            if match:
                self.shared_state.progress += 1
                self.shared_state.progress_percentage = (self.shared_state.progress / self.shared_state.total_parts) * 100
                self.worker_progress.emit(self.worker_name, self.shared_state.progress_percentage)
                QApplication.processEvents()
                
        except Exception:
            self.handleError(record)

class Converter(QObject):
    """
    Handles the text-to-speech (TTS) conversion process for PDF and text files.
    Signals:
        op_msgs: Emits messages about the status of the TTS process. Connects to log_widget.
        worker_progress: Updates the value of the progress bar during TTS. Connects to progress_widget.
        revise_worker_label: Updates the label of the progress bar during TTS. Connects to progress_widget.
        worker_done: Signals the completion of the TTS process. Connects to progress_widget.
    """
    op_msgs = Signal(str)
    worker_progress = Signal(str, int)
    revise_worker_label = Signal(str, str)
    worker_done = Signal(str)
    def __init__(self):
        super().__init__()
    def convert(self, file_tree, pdf):
        """
        Converts the specified PDF or text file to speech using Google Text-to-Speech (gTTS).
        Args:
            file_tree (QWidget): The file tree widget where output files may be added.
            pdf (str): Path of the PDF or text file to convert to speech.
        Notes:
            - Emits a message if the provided file is not a PDF or text file.
            - Initializes shared state and sets up logging for progress tracking.
            - Uses gTTS to perform TTS conversion on the file.
            - Emits progress updates and completion signals during the TTS process.
        """
        if not any(pdf.lower().endswith(ext) for ext in ['.pdf', '.txt']):
            self.op_msgs.emit(f"Cannot TTS. Filetype is not TXT or PDF.")
            return
        self.settings = SettingsWindow.instance()
        self.op_msgs.emit(f"Converting {pdf}")

        shared_state = SharedState()

        worker_name = f"TTS_{pdf}"
        self.worker_progress.emit(worker_name, 0)

        logger = logging.getLogger('gtts.tts')
        logger.setLevel(logging.DEBUG)
        handler = QueueHandler(shared_state, self.op_msgs, self.worker_progress, self.revise_worker_label, worker_name)
        logger.addHandler(handler)

        try:
            text = clean_text(pdf)
            if self.settings.split_txt_checkbox.isChecked():
                temp_file = os.path.join(self.get_temp_dir(), "tts-tempfile.txt")
                output_paths = tts_word_count(text, temp_file, True)
                output_count = len(output_paths)
                count = 0
                for output_path in output_paths:
                    count += 1
                    self.revise_worker_label.emit(worker_name, f"TTS ({count}/{output_count})")
                    with open(output_path, 'r', encoding='utf-8') as txt_file:
                        text = txt_file.read()
                    tts = gTTS(text, lang='en', tld='us')
                    output_file = construct_filename(pdf, "tts_ps")
                    tts.save(output_file)
                    self.op_msgs.emit(f"Conversion {count}/{output_count} complete. Output: {output_file}")
                    self.worker_progress.emit(worker_name, 0)
                    shared_state.progress = 0
                    shared_state.total_parts = 0 
                    shared_state.progress_percentage = 0
                    os.remove(output_path)
            else:
                tts = gTTS(text, lang='en', tld='us')
                output_file = construct_filename(pdf, "tts_ps")
                tts.save(output_file)
                self.op_msgs.emit(f"Conversion complete. Output: {output_file}")
        except Exception as e:
            error_msg = f"Error converting {pdf}: {str(e)}"
            self.op_msgs.emit(error_msg)
        self.worker_done.emit(worker_name)
        logger.disabled = True
        logger.removeHandler(handler)
        handler.close()

    def get_temp_dir(self):
        """
        Check if the temp directory exists. If not, create it. Return the temp directory path.
        Returns:
            str: The path to the temp directory.
        """
        project_root = QDir.currentPath()
        temp_directory = os.path.join(project_root, "temp")
        if not os.path.isdir(temp_directory):
            os.mkdir(temp_directory)
        return temp_directory

tts = Converter()