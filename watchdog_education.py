from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event): # İçerikte değişiklik olduğu anda çalışır 
        if not event.is_directory:
            print(f'File modified: {event.src_path}')
    
    def on_created(self, event): # Yeni bir dosya oluşturulduğunda çalışır
        if not event.is_directory:
            print(f'File created: {event.src_path}')
    
    def on_deleted(self, event): # Bir dosya silindiğinde çalışır
        if not event.is_directory:
            print(f'File deleted: {event.src_path}')
    
    def on_moved(self, event): # Bir dosya taşındığında çalışır
        if not event.is_directory:
            print(f'File moved from {event.src_path} to {event.dest_path}')

my_folder = "./"
handler = MyHandler()
observer = Observer()
observer.schedule(handler, my_folder, recursive=False) # Klasör içindeki değişiklikleri izler

observer.start() # İzleme işlemini başlatır
print(f"observing başlatıldı: {my_folder}")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("observing durduruluyor...")
    observer.stop() # İzleme işlemini durdurur

observer.join() # İzleme işleminin tamamen durmasını bekler