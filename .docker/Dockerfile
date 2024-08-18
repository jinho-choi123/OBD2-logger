FROM python:3.11.9

# install OBD emulator
RUN python3 -m pip install ELM327-emulator 

CMD ["elm", "-s", "car", "-a" , "115200"]