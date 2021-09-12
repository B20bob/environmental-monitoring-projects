

# How to configure Raspberry Pi to use Waveshare B 5" TFT LCD:
https://www.waveshare.com/wiki/5inch_HDMI_LCD_(B)

    Raw info:

    Working with Raspberry Pi
    This LCD can support Raspbian / Ubuntu / Kali / Retropie and WIN10 IoT systems. When the LCD works on systems such as Raspberry Pi, the resolution must be set manually, otherwise, it will cause abnormal display. There is no such problem when the LCD works on the PC version of Windows.

    Please download the latest version of the image on the Raspberry Pi official website.

    1) Download the compressed file to the PC, and unzip it to get the .img file.

    2) Connect the TF card to the PC, use SDFormatter.exe software to format the TF card.

    3) Open the Win32DiskImager.exe software, select the system image downloaded in step 1, and click‘Write’ to write the system image.

    4) After the image has finished writing, open the config.txt file in the root directory of the TF card, add the following code at the end of config.txt, then save and quit the TF card safely.

    max_usb_current=1
    hdmi_group=2
    hdmi_mode=87
    hdmi_cvt 800 480 60 6 0 0 0  
    hdmi_drive=1
    You must make sure that there are no spaces on either side of the equal sign.

    5) Insert the TF card into the Raspberry Pi.

    6) Turn on the backlight switch on the back of the LCD.

    7) Connect the Touch interface of the LCD to the USB interface of the Raspberry Pi.

    8) Connect the HDMI interface of the LCD to the HDMI interface of the Raspberry Pi, power on the Raspberry Pi, and wait for a few seconds until the LCD displays normally.

    Note: Resolution of Ubuntu Mate OS or Windows 10 IoT Core OS can also be set properly by editing config.txt.

    Calibration in Raspbian
    If a latest Raspbian OS is in used, you should connect your Pi to the internet and install xserver-xorg-input-evdev.

    sudo apt-get install xserver-xorg-input-evdev
    Just be sure that evdev.conf has a higher number than 40-libinput.conf. For example, rename 10-evdev.conf to 45-evdev.conf. this forces evdev to load after libinput.
    sudo cp -rf /usr/share/X11/xorg.conf.d/10-evdev.conf /usr/share/X11/xorg.conf.d/45-evdev.conf
    sudo reboot
    This LCD can be calibrated using a program called xinput_calibrator and you should get and install the program manually with

    sudo apt-get install -y xinput-calibrator
    Enter the following commands for touch screen calibration:

    sudo DISPLAY=:0.0 xinput_calibrator
    or select Menu -> Preferences -> Calibrate Touchscreen.

    After running these commands, there will be a prompt for four-point calibration shown in the LCD screen. Click the points one by one to finish the touch calibration. Then, the new calibration data will be displayed in the terminal, such as the following data. Please save these data for future use.

    Doing dynamic recalibration:
    Setting new calibration data: 3919, 208, 236, 3913
    Enter the following command to edit 40-libinput.conf:

    sudo nano /usr/share/X11/xorg.conf.d/40-libinput.conf
    Save the touch parameters (may differ depending on LCD) to the end of 40-libinput.conf, as shown in the picture:

    5inch HDMI LCD FAQ1.jpg

    Press the keys Ctrl+X, and select the option Y to save the modification.

    The modification will be valid after rebooting the system. Enter the following command for system reboot:

    sudo reboot