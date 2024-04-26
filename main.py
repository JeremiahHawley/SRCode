import qrcode
def create_qrcode(data,filename,Ver_val):
    #create the qrcode object
    object = qrcode.QRCode(
        #set version of the qrcode
        version=Ver_val,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
    )
    #set object data
    object.add_data(data)
    #create the qrcode
    object.make(fit=True)
    img = object.make_image(fill_color="black", back_color="white")
    #save the qrcode as the provided filename
    img.save(str(filename))

path_to_bytecode = "TEST.txt"

file_path = "test.png"
file_data = open(path_to_bytecode,"rb").read()
create_qrcode(file_data,file_path,1)