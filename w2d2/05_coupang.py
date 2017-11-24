from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

# 쿠팡 로그인 페이지
driver.get('https://login.coupang.com/login/login.pang')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#login-email-input').send_keys('')
driver.find_element_by_css_selector('#login-password-input').send_keys('')
driver.find_element_by_css_selector('form').submit()

time.sleep(3)

# 로켓 배송 목록보기
driver.get('http://www.coupang.com/np/rocketdelivery')

# 목록 가져오기
goods_list = driver.find_elements_by_css_selector('a.baby-product-link')
for goods in goods_list:
    try:
        goods_name = goods.find_element_by_css_selector('div.name')
        goods_price = goods.find_element_by_css_selector('strong.price-value')
        print(f"{goods_name.text} : {goods_price.text}")
    except Exception as e:
        pass

# 내 주문목록 가져오기 
driver.get('https://my.coupang.com/purchase/list')

order_list = driver.find_elements_by_css_selector(
    'div.my-order-unit__item-info > a'
)

for order in order_list:
    print('상품명: ', order.find_element_by_css_selector(
            'div > strong:nth-of-type(2)').text
        )
    print('상품링크: ', order.get_attribute("href"))

driver.quit()
