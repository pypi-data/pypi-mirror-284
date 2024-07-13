import sys
try:
    import sounddevice as sd
except ImportError as e:
    print("Please install sounddevice first. You can use")
    print()
    print("  pip install sounddevice")
    print()
    print("to install it")
    sys.exit(-1)
import sherpa_ncnn
import threading
from queue import Queue
import time


class STT():
    def __init__(self,duration=4,mode='zh-en') -> None:
        if mode!='chinese' and mode!='english' and mode!='zh-en':
            print('please input chinese or english or zh-en')
            return       
        self.mode = mode
        self.last = ''
        self.wordList = Queue()
        self.recognizer = None
        self.stop = False
        self.t1 = None
        self.t2 = None
        self.duration = duration

    def create_recognizer(self):
        # Please replace the model files if needed.
        # See https://k2-fsa.github.io/sherpa/ncnn/pretrained_models/index.html
        # for download links.
        recognizer = sherpa_ncnn.Recognizer(
            tokens=f"./hqx/sherpa/{self.mode}/tokens.txt",
            encoder_param=f"./hqx/sherpa/{self.mode}/encoder_jit_trace-pnnx.ncnn.param",
            encoder_bin=f"./hqx/sherpa/{self.mode}/encoder_jit_trace-pnnx.ncnn.bin",
            decoder_param=f"./hqx/sherpa/{self.mode}/decoder_jit_trace-pnnx.ncnn.param",
            decoder_bin=f"./hqx/sherpa/{self.mode}/decoder_jit_trace-pnnx.ncnn.bin",
            joiner_param=f"./hqx/sherpa/{self.mode}/joiner_jit_trace-pnnx.ncnn.param",
            joiner_bin=f"./hqx/sherpa/{self.mode}/joiner_jit_trace-pnnx.ncnn.bin",
            num_threads=4,
            hotwords_file="",
            hotwords_score=1.5,
        )
        return recognizer


    def recoder(self):
        print("Started! Please speak")
        self.recognizer = self.create_recognizer()
        self.recognizer.reset()
        sample_rate = self.recognizer.sample_rate
        samples_per_read = int(0.1 * sample_rate)  # 0.1 second = 100 ms
        last_result = ""
        with sd.InputStream(channels=1, dtype="float32", samplerate=sample_rate) as s:
            while not self.stop:
                samples, _ = s.read(samples_per_read)  # a blocking read
                samples = samples.reshape(-1)
                self.recognizer.accept_waveform(sample_rate, samples)
                result = self.recognizer.text
                if last_result != result:
                    last_result = result
                    self.last = result
                    self.wordList.put(result)
                    # print("\r{}".format(result), end="")

    def start(self):    
        self.t1 = threading.Thread(target=self.recoder,daemon=True)
        self.t2 = threading.Thread(target=self.check,daemon=True)
        self.t1.start()
        self.t2.start()
    def check(self):
        while not self.stop:
            time.sleep(self.duration)
            if self.wordList.empty():
                self.recognizer.reset()
    def updata(self):
        while self.wordList.empty():
            pass
        return self.wordList.get()
    
    def getword(self):
        word = ''
        while True:
            now = self.updata()
            if len(now)>0:
                word = now
            else:
                return word

    def close(self):
        self.stop = True
        self.t1.join()
        self.t2.join()
        print('录音程序已结束')

    # devices = sd.query_devices()
    # # print(devices)
    # default_input_device_idx = sd.default.device[0]
    # print(f'Use default device: {devices[default_input_device_idx]["name"]}')
    # recoder()

