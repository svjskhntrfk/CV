from flask import Flask, render_template, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sosiska'

TRANSLATIONS = {
    'ru': {
        'name' : 'Вероника Дмитренко',
        'theme_switch': 'Переключить тему',
        'lang_switch': 'Switch to English',
        'greeting': 'Привет! Меня зовут Вероника',
        'role': 'Студенточка',
        'about_me': 'Вкратце обо мне',
        'experience': 'Мой опыт работы',
        'collaboration': 'Сотрудничество',
        'write_me': 'Написать мне',
        'bio': 'Я — студентка 2 курса ОП Экономика и анализ данных в НИУ ВШЭ, \nУчусь хорошо, мечтаю начать ходить на все лекции.',
        'about_section': 'Обо мне',
        'about_text': 'Кроме учебы я активно участвую в кейс-чемпионатах, где еще и часто занимаю призовые места',
        'about_text2': 'Люблю солнце, море и песок',
        'work_experience': 'Мой опыт работы',
        'time_cmwp' : 'Июль 2024 – Настоящее время',
        'intern_analyst': 'Стажер - аналитик',
        'work_cmwp': 'Анализирую и подготавливаю данные для составления стратегий развития бизнеса',
        'hse' :'НИУ ВШЭ',
        'time_hse' : 'Сентябрь 2022 – Настоящее время',
        'student': 'Студентка',
        'work_hse' : 'Учу экономику, математику и программирование',
        'goals': 'Мои цели',
        'goals_text': 'Найти работу(желательно оплачиваемую)',
        'collaboration_text': 'Если интересно, что я могу для вас сделать, пишите:',
        'telegram': 'Написать в Telegram',
        'resume': 'Посмотреть резюме',
        'email': 'Написать на почту',
        'footer': 'Cделано с любовью в 2024 году.'
    },
    'en': {
        'name' : 'Veronika Dmitrenko',
        'theme_switch': 'Toggle theme',
        'lang_switch': 'Переключить на русский',
        'greeting': 'Hi! My name is Veronika',
        'role': 'Student',
        'about_me': 'About me',
        'experience': 'Work Experience',
        'collaboration': 'Collaboration',
        'write_me': 'Contact me',
        'bio': "I'm a 2nd year student at HSE University, studying Economics and Data Analysis. \nI'm doing well in my studies and dream of attending all lectures.",
        'about_section': 'About me',
        'about_text': 'Besides studying, I actively participate in case championships, where I often win prizes',
        'about_text2': 'I love sun, sea and sand',
        'work_experience': 'Work Experience',
        'time_cmwp' : 'July 2024 – now',
        'intern_analyst': 'Intern Analyst',
        'work_cmwp': 'I analyze and prepare data for the preparation of business development strategies',
        'hse' :'Higher School of Economics',
        'time_hse' : 'September 2022 – now',
        'student': 'Student',
        'work_hse' : 'I study economics, mathematics and programming.',
        'goals': 'My Goals',
        'goals_text': 'Find a job (preferably paid)',
        'collaboration_text': 'If you are interested in what I can do for you, write to me:',
        'telegram': 'Message on Telegram',
        'resume': 'View Resume',
        'email': 'Send Email',
        'footer': 'Made with love in 2024'
    }
}

@app.route("/")
def main():
    time_cur = datetime.now().hour
    if 'theme' not in session:
        if time_cur > 18 or time_cur < 6:
            session['theme'] = 'dark-theme'
        else:
            session['theme'] = 'light-theme'
    if 'lang' not in session:
        session['lang'] = 'ru'
    return render_template("index.html", 
                         theme=session['theme'], lang=session['lang'], t=TRANSLATIONS[session['lang']])

@app.route("/change_theme")
def toggle_theme():
    if session.get('theme') == 'dark-theme':
        session['theme'] = 'light-theme'
    else:
        session['theme'] = 'dark-theme'
    return redirect("/")

@app.route("/change_lang")
def toggle_lang():
    if session.get('lang') == 'ru':
        session['lang'] = 'en'
    else:
        session['lang'] = 'ru'
    return redirect("/")

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
