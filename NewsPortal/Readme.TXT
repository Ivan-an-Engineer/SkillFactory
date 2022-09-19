#ПЕРВО-НАПЕРВО:
venv\scripts\activate
cd NewsPaper
python manage.py makemigrations
python manage.py migrate
python manage.py shell

#Далее команды в Shell:
from news.models import *

#Добавляем пользователей
Andrew_user = User.objects.create_user(username='Andrew', email='Andrew@email.ru', password='Andrew_password')
Stan_user = User.objects.create_user(username='Stan', email='Stan@email.ru', password='Stan_password')

#Добавляем авторов
Andrew = Author.objects.create(author_user=Andrew_user)
Stan = Author.objects.create(author_user=Stan_user)

#Добавляем категории
Sport = Category.objects.create(title='Спорт')
Politics = Category.objects.create(title='Политика')
Economics = Category.objects.create(title='Экономика')
War = Category.objects.create(title='Война')

#Далее идут статьи и новость

About_Dictators = Post.objects.create(post_author=Stan, post_choice=Post.article, post_title='О том, как стать диктатором', post_text='''
(◡̀_◡́)ᕤ Здравствуйте, меня зовут Максим Саморуков. Я журналист, специализирующийся на Восточной Европе, и эксперт «Фонда Карнеги за международный мир».
В своем прошлом письме для Kit я рассказывал, как начинаются войны и почему люди до сих пор воюют.
В начале июля редакция снова написала мне — и попросила составить что-то вроде досье на современного диктатора. Как вообще ими становятся? По какой причине лидеры многих стран не хотят быть конструктивными и законопослушными политиками?
Почему они готовы репрессировать и вести неправедные войны, лишь бы удержать власть, а не просто уходят на пенсию, отработав положенное?
Все эти вопросы действительно звучат на фоне многих мировых событий (а сейчас особенно). Но я сразу сказал редакции, что досье составить не смогу.
Потому что уверен: нельзя списывать диктаторство на детские комплексы, сложные отношения с родителями или школьные обиды. На какие-то особенные личные качества — пожалуй, тоже.
Превращение в диктатора — процесс гораздо менее зловещий, чем может показаться. И куда большую роль, чем личные качества человека, в нем играют внешние обстоятельства.
В общем, мое сегодняшнее письмо не о некоем среднем узурпаторе, а, скорее, о его пути. Часто это путь наименьшего сопротивления без ясных альтернатив (по крайней мере, если смотреть глазами правителя).
Нет, я не буду выступать адвокатом диктаторов или выставлять их жертвами обстоятельств. Я хочу показать: именно потому, что они не какие-то особенные люди, диктатура чрезвычайно живуча. Она способна возвращаться вновь и вновь, несмотря на все свои многочисленные провалы в прошлом...''')

About_Literature = Post.objects.create(post_author=Andrew, post_choice=Post.article, post_title='О роли литературы', post_text='''
(•̀ᴗ•́ )و Здравствуйте, это Андрей Перцев — корреспондент ________, который много лет пишет о российской политике.
В начале лета Владимир Путин, который вообще очень любит порассуждать об истории, в очередной раз выступил с монологом на эту тему. На встрече с предпринимателями, инженерами и учеными президент заявил, что император Петр Первый вел войну со Швецией не для того, чтобы «отторгать» у нее территории, а чтобы «вернуть» свое. «На нашу долю тоже выпало возвращать и укреплять», — сделал вывод Путин и ухмыльнулся.
Вероятно, все эти годы исторические взгляды президента вас мало интересовали. Ну считает Путин распад СССР «трагедией», ну находит в этой трагедии виновных (того же Ленина или Михаила Горбачева) — что с того? В феврале 2022-го стало понятно, насколько эти взгляды важны. Авторитарный лидер, которого очень беспокоят исторические «ошибки» прошлого, принялся «исправлять» их артиллерией, танками и кровью.
Это и есть настоящая трагедия. И все эти месяцы мы в той или иной степени пытаемся понять его логику — чтобы хоть как-то объяснить себе безумие происходящего. Я тоже много думаю об этом — не только в контексте логики самого Путина, но и в контексте логики истории. В своем сегодняшнем письме я расскажу, что в этой логике Путин не одинок. Мы с вами смотрим на историю похожим образом (такая уж эпоха). А еще покажу, насколько идеи об исправлении «ошибок» прошлого популярны в российском обществе — и какую роль в этом сыграла «плохая» фантастическая литература.''')

First_Sports = Post.objects.create(post_author=Stan, post_title='Обладатель Гран-при Каннского фестиваля снимет фильм о петербургском баскетболе', post_text='''Съемки документального фильма о петербургском баскетболе планируется начать 15 сентября.
Оператором ленты выступил Павел Фоминцев, ставший обладателем Гран-при программы «Особый взгляд» Каннского фестиваля-2021 за фильм «Разжимая кулаки».
Большая часть фильма будет посвящена Кубку Кондрашина и Белова, который пройдет в Петербурге 17 и 18 сентября. Помимо этого в ленте расскажут о легендарном тренере Владимире Кондрашине и его не менее легендарном воспитаннике — Александре Белове, в честь которых назван Кубок.''')

#Далее добавляются категории к статьям и новости (Это разные варианты, найденные на просторах сети)
About_Dictators_category = PostCategory.objects.create(post=About_Dictators, category=Politics)
About_Literature.post_category.add(Politics, War)
First_Sports.post_category.add(Sport)

#Добавляются комментарии:
First_Comment = Comment.objects.create(comment_post=About_Dictators, comment_user=Andrew_user, comment_text='Интересная статья')
Second_Comment = Comment.objects.create(comment_post=About_Dictators, comment_user=Stan_user, comment_text='Обязательно к почтению!')
Third_Comment = Comment.objects.create(comment_post=About_Literature, comment_user=Stan_user, comment_text='Хахахаха')
Fourth_Comment = Comment.objects.create(comment_post=First_Sports, comment_user=Andrew_user, comment_text='И зачем тут это???')

#Лайки-Дизлайки:
for i in range(10):
    About_Dictators.like()

for i in range(6):
    About_Literature.like()

for i in range(3):
    First_Sports.dislike()

First_Comment.like()
Second_Comment.like()
Third_Comment.dislike()
Fourth_Comment.like()
Fourth_Comment.dislike()

#Обновляем рейтинги пользователей:
Andrew.update_rating()
Stan.update_rating()

#Ищем лучшего автора:
best_author = Author.objects.all().order_by('-author_rating')[0]
print(f'Лучший автор - {best_author.author_user.username}')

#Ищем лучшую статью:
best_article = Post.objects.filter(post_choice=Post.article).order_by('-post_rating')[0]
print(f'Лучшая статья добавлена {best_article.post_date.strftime("%d.%m.%Y")} автором {best_article.post_author.author_user.username}, рейтинг статьи - {best_article.post_rating}. Заголовок: "{best_article.post_title}". Превью: {best_article.preview()}')

#Выводим комментарии к лучшей статье:
for _comment in Comment.objects.filter(comment_post=best_article):
    print(f'{_comment.comment_date.strftime("%d.%m.%Y")} {_comment.comment_user.username} *{_comment.comment_rating}*: {_comment.comment_text}')
