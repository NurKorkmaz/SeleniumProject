from selenium import webdriver
import time

driver_path = "/home/nur/Desktop/Python/yeni/selenium/chromedriver"

driver = webdriver.Chrome(driver_path)

driver.get("https://www.youtube.com/channel/UCPJJbWeR2r1Rs_FWQhsPaFw/videos")
driver.maximize_window()
driver.save_screenshot("/home/nur/Desktop/test.png")
abone_sayisi = driver.find_element_by_id("subscriber-count").text
print(abone_sayisi) 


dosya = open("/home/nur/Desktop/odev_1.txt","w")
dosya.write(driver.title)
dosya.write(' - ')
dosya.write(abone_sayisi)
dosya.write('\n')


liste1 = driver.find_elements_by_id("video-title")
liste2 = driver.find_elements_by_css_selector("#metadata-line > span:nth-child(1)")
for i in range(len(liste1)):
    for j in range(len(liste2)):
        if i == j :
            goruntuleme_sayisi = liste2[j].text
            video_adi = liste1[i].text
            break
    print(goruntuleme_sayisi, video_adi)
    dosya.write(goruntuleme_sayisi)
    dosya.write(' - ')
    dosya.write(video_adi)
    dosya.write('\n')
    dosya.close
 
time.sleep(5)
driver.quit()