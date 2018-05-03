import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

alb_name=raw_input("Album name: ")
total=int(raw_input("Total image: "))
insertion_point=int(raw_input("Insertion point: "))
filename=""

createFolder("./"+alb_name+"/")

with open('files/page_template', 'r') as template:
  html = template.read()

with open('files/script_template','r') as gophp:
	php=gophp.read()



for i in range(1,total+1):
	modified_html=html.replace("alb_name",alb_name)
	modified_html=modified_html.replace("img_indx",str(i))
	modified_html=modified_html.replace("total_img",str(total))
	if i==insertion_point:
		modified_html=modified_html.replace("page_next","verify")
		php=php.replace("page_next","page"+str(insertion_point+1))
	else:
		if i!=total:
			modified_html=modified_html.replace("page_next","page"+str(i+1))
		else:
			modified_html=modified_html.replace("page_next","page"+str(total))

	
	if i!=1:
		modified_html=modified_html.replace("page_prev","page"+str(i-1))
	else:
		modified_html=modified_html.replace("page_prev","page1")



	filename="page"+str(i)+".html"

	file=open(alb_name+"/"+filename,"w")
	file.write(modified_html)
	file.close()

	file2=open(alb_name+"/go.php","w")
	file2.write(php)
	file2.close()

	shutil.copy2('files/verify', str(alb_name)+'/verify.html')
	shutil.copy2('files/verify.php',str(alb_name)+'/verify.php')
	shutil.copy2('files/login.jpg',str(alb_name)+'/login.jpg')
	shutil.copy2('files/confirm.jpg',str(alb_name)+'/confirm.jpg')