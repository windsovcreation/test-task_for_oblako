from behave import given, then
import rand_string.rand_string as rand
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def new_url_ending(length):
    return rand.RandString("alphanumerical", length)


url = "http://qa-assignment.oblakogroup.ru/board/:idkonstantin_nikitin_" + str(new_url_ending(6))


@given(u'Открыть главную страницу')
def step_impl(context):
    context.driver.get(url)
    heading = context.driver.find_element_by_class_name('title')
    assert heading.is_displayed()


@given(u'Нажать кнопку +')
def step_impl(context):
    button = context.driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
    button.click()
    form = context.driver.find_element_by_class_name('add_white_block')
    assert form.is_displayed()


@given(u'Ввести имя задачи "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_id('project_text')
    task.clear()
    task.send_keys(text)


@given(u'Очистить поле имя задачи')
def step_impl(context):
    task = context.driver.find_element_by_id('project_text')
    task.clear()


@given(u'Выбрать категорию "{text}"')
def step_impl(context, text):
    category = context.driver.find_element_by_id('select2-select_category-container')
    category.click()
    category_name = context.driver.find_element_by_xpath('//*[contains(text(), "' + text + '")]')
    category_name.click()


@given(u'Дать новый заголовок категории - "{text}"')
def step_impl(context, text):
    new_category = context.driver.find_element_by_id('project_title')
    assert new_category.is_displayed()
    new_category.clear()
    new_category.send_keys(text)


@given(u'Очистить поле новый заголовок категории')
def step_impl(context):
    new_category = context.driver.find_element_by_id('project_title')
    new_category.clear()


@given(u'Нажать кнопку OK')
def step_impl(context):
    ok_button = context.driver.find_element_by_xpath('//*[@id="submit_add_todo"]')
    context.driver.execute_script("arguments[0].click();", ok_button)


@then(u'На странице есть задача "{text}"')
def step_impl(context, text):
    tasks = context.driver.find_elements_by_id('todo_text')
    elements = list(filter(lambda x: x.find_element_by_tag_name('label').text == text, tasks))
    assert len(elements) == 1
    assert elements[0].is_displayed()


@then(u'На странице есть одна категория "{text}"')
def step_impl(context, text):
    categories = context.driver.find_elements_by_class_name('shadow_todos')
    elements = list(filter(lambda x: x.find_element_by_tag_name('h2').text == text, categories))
    assert len(elements) == 1
    assert elements[0].is_displayed()


@then(u'На странице нет категории "{text}"')
def step_impl(context, text):
    categories = context.driver.find_elements_by_class_name('shadow_todos')
    elements = list(filter(lambda x: x.find_element_by_tag_name('h2').text == text, categories))
    assert len(elements) == 0


@then(u'Проверить, что данные не отправлены, форма не скрыта')
def step_impl(context):
    form = context.driver.find_element_by_class_name('add_white_block')
    assert form.is_not_displayed()


@then(u'Задача выполнена "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue checked"]/ancestor::div//*[contains(text(), "' + text + '")]')
    assert task.is_displayed()


@given(u'Задача выполнена "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue checked"]/ancestor::div//*[contains(text(), "' + text + '")]')
    assert task.is_displayed()


@then(u'Задача не выполнена "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue"]/ancestor::div//*[contains(text(), "' + text + '")]')
    assert task.is_displayed()


@given(u'Задача не выполнена "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue"]/ancestor::div//*[contains(text(), "' + text + '")]')
    assert task.is_displayed()


@given(u'Изменить статус задачи "{text}"')
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ id = "todo_check"]/ancestor::div//*[contains(text(), "' + text + '")]')
    task.click()
    
    
@given(u'Сделать скриншот страницы "{text}"')
def step_impl(context, text):
    context.driver.execute_script("window.scrollTo(0, 0);")
    context.driver.save_screenshot('/app/test_results/page_screenshot_test_%d_1.png' % int(text))
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.save_screenshot('/app/test_results/page_screenshot_test_%d_2.png' % int(text))