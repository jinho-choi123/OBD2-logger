import obd 

def log_rpm(r):
    print(f'timestamp {r.time} | RPM {r.value}')



if __name__ == "__main__":
    connection = obd.Async(fast=False, timeout=30)

    # query a command

    connection.watch(obd.commands.RPM, callback=log_rpm)

    connection.start()

    # FIXME
    # test for just 60 seconds 
    
    connection.stop()



