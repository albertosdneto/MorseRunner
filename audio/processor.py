### processor.py
import os
import wave


class WavFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.wave_file = None
        self.is_open = False
        self.samples_per_sec = None
        self.n_channels = None

    def open_read(self):
        """
        Opens a WAV file for reading and loads its audio metadata.
        """
        if not os.path.exists(self.file_name):
            raise Exception(f"File {self.file_name} does not exist.")

        try:
            # Open wav file in read mode
            self.wave_file = wave.open(self.file_name, "rb")
            self.samples_per_sec = self.wave_file.getframerate()
            self.n_channels = self.wave_file.getnchannels()
            self.is_open = True
        except Exception as e:
            raise Exception(f"Error opening file: {str(e)}")

    def open_write(self, samples_per_sec=11025, stereo=False):
        """
        Prepares the instance for writing audio data.
        """
        try:
            self.samples_per_sec = samples_per_sec
            self.n_channels = 2 if stereo else 1
            self.wave_file = wave.open(self.file_name, "wb")
            self.wave_file.setnchannels(self.n_channels)
            self.wave_file.setsampwidth(2)  # 16-bit audio
            self.wave_file.setframerate(self.samples_per_sec)
            self.is_open = True
        except Exception as e:
            raise Exception(f"Error preparing file for write: {str(e)}")

    def read(self):
        """
        Reads a block of audio data from the WAV file.
        """
        if not self.is_open or self.wave_file is None:
            raise Exception("File is not open for reading.")
        try:
            return self.wave_file.readframes(self.wave_file.getnframes())
        except Exception as e:
            raise Exception(f"Error reading audio data: {str(e)}")

    def write(self, audio_data):
        """
        Writes audio data to the WAV file.
        """
        if not self.is_open or self.wave_file is None:
            raise Exception("File is not open for writing.")
        try:
            self.wave_file.writeframes(audio_data)
        except Exception as e:
            raise Exception(f"Error writing audio data: {str(e)}")

    def save(self):
        """
        Saves (closes) the WAV file if open.
        """
        if self.wave_file:
            self.wave_file.close()
            self.is_open = False

    def close(self):
        """
        Closes the WAV file and resets the instance state.
        """
        if self.wave_file:
            self.wave_file.close()
        self.wave_file = None
        self.is_open = False
