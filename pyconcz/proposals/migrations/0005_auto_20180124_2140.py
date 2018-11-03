# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0004_auto_20180116_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='final_note',
            field=models.TextField(blank=True, null=True, verbose_name='Anything else you want to tell us?'),
        ),
        migrations.AddField(
            model_name='talk',
            name='referral_link',
            field=models.TextField(blank=True, default='', help_text='If you already have a recording of you giving a talk, you can paste the link here.', verbose_name='Got a video?'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='final_note',
            field=models.TextField(blank=True, null=True, verbose_name='Anything else you want to tell us?'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='referral_link',
            field=models.TextField(blank=True, default='', help_text='If you have a recording of you giving a talk or leading a workshop, you can paste the link here.', verbose_name='Got a video?'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='requirements',
            field=models.TextField(blank=True, help_text='Do you have any special requirements? What do attendees need to bring? Do you need anything more than a room with wifi, standard euro sockets and a projector?', null=True, verbose_name='Extra requirements'),
        ),
        migrations.AlterField(
            model_name='financialaid',
            name='email',
            field=models.EmailField(help_text='We’ll keep it secret, for internal use only.', max_length=254),
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=models.TextField(help_text='Introduce the problem your talk will bring a solution to. Then explain why it’s a problem worth solving and use the last paragraph to tell your audience what is your approach to solving it.', verbose_name='Tell the audience about your talk in 1–3 paragraphs (90–200 words)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='bio',
            field=models.TextField(help_text='Tell your audience in first person about anything relevant about you, whether it’s your background, education, experience, current or former employer, hobbies or opensource software you maintain.\nTry keeping it between between 50 and 90 words.\nYou can of course include anything fun or quirky about yourself.', verbose_name='Why you are the right person to talk about the topic you chose?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner  (suitable for everyone)'), ('advanced', 'Advanced  (requires a high level of Python knowledge)')], default='beginner', max_length=10),
        ),
        migrations.AlterField(
            model_name='talk',
            name='email',
            field=models.EmailField(help_text='We’ll keep it secret, for internal use only.', max_length=254, verbose_name='Your email address'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Please state explicitly:\n1) why you need it,\n2) what for and\n3) how much in Euros.\nIf you require aid for more items (accomodation, travel costs etc.) please state the amount for each item.', null=True, verbose_name='Details about required financial aid'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='full_name',
            field=models.CharField(help_text='This will be published in the schedule, so use a name that you’re comfortable with, or a nickname.', max_length=200, verbose_name='What’s your name?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='github',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='GitHub username'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='language',
            field=models.CharField(choices=[('en', 'English (preferred)'), ('cs', 'Czech or Slovak')], default='en', help_text='English is preferred, but if you feel uncomfortable with it, you can give your talk in Czech or Slovak', max_length=2),
        ),
        migrations.AlterField(
            model_name='talk',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Covering travel or accommodation costs etc. Please specify this here and now, otherwise we might not be able to grant you the aid.', verbose_name='I need financial aid to make this talk possible'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='photo',
            field=models.ImageField(help_text='It will be published on the website.\nIdeal photo is: a head shot, shows only you, has no “filters” applied and is as large and uncompressed as possible.\nWe might crop it and change contrast, brightness etc. to fit PyCon CZ visual style.', upload_to='proposals/pyconcz2018/talks/', verbose_name='Your photo (not an\xa0illustration nor\xa0avatar)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(help_text='This will be published everywhere! Make up some catchy title which will attract the audience.', max_length=200, verbose_name='What is the title of your talk?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='abstract',
            field=models.TextField(help_text='Describe your workshop or sprint.\nPlease include the requirements: libraries and Python version to be installed, required experience with topics/libraries, etc.', verbose_name='Tell the audience about your talk in 1–3 paragraphs (90–200 words)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='bio',
            field=models.TextField(help_text='Tell your audience in first person about anything relevant about you, whether it’s your background, education, experience, current or former employer, hobbies or opensource software you maintain.\nTry keeping it between between 50 and 90 words.\nYou can of course include anything fun or quirky about yourself.', verbose_name='Why you are the right person to talk about the topic you chose?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner  (suitable for everyone)'), ('advanced', 'Advanced  (requires a high level of Python knowledge)')], default='beginner', max_length=10),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='email',
            field=models.EmailField(help_text='We’ll keep it secret, for internal use only.', max_length=254, verbose_name='Your email address'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Please state explicitly:\n1) why you need it,\n2) what for and\n3) how much in Euros.\nIf you require help for more items (accomodation, travel costs etc.) please state the amount for each item.', null=True, verbose_name='Details about required financial aid'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='full_name',
            field=models.CharField(help_text='This will be published in the schedule, so use a name that you’re comfortable with, or a nickname.', max_length=200, verbose_name='What’s your name?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='github',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='GitHub username'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='language',
            field=models.CharField(choices=[('en', 'English (preferred)'), ('cs', 'Czech or Slovak')], default='en', max_length=2),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='length',
            field=models.CharField(blank=True, choices=[('1h', '1 hour'), ('2h', '2 hours'), ('2h', '3 hours'), ('1d', 'Full day (most sprints go here!)'), ('xx', 'Something else! (Please leave a note in the abstract)')], help_text='Sprints usually take the whole day, but workshops are organized in smaller blocks. You can also have a full-day workshop with lunch break, but keep in mind that the length could discourage attendees.', max_length=2, verbose_name='How much time does your workshop take?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Covering travel or accommodation costs etc. Please specify this here and now, otherwise we might not be able to grant you the aid.', verbose_name='I need financial aid to make this workshop possible'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='photo',
            field=models.ImageField(help_text='It will be published on the website.\nIdeal photo is: a head shot, shows only you, has no “filters” applied and is as large and uncompressed as possible.\nWe might crop it and change contrast, brightness etc. to fit PyCon CZ visual style.', upload_to='proposals/pyconcz2018/talks/', verbose_name='Your photo (not an\xa0illustration nor\xa0avatar)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(help_text='Public title. What topic/project is it all about?', max_length=200, verbose_name='What is the title of your workshop or sprint?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='type',
            field=models.CharField(choices=[('workshop', 'Workshop'), ('sprint', 'Sprint')], default='sprint', help_text='At a workshop, you should present hands-on exercises for participants to learn from. You’ll get a room and a slot in the agenda, and participants will need to register.\nAt a sprint, participants help an open-source project – usually by cloning the repo and trying to fix beginner-level issues, while you’ll provide one-to-one mentorship. If several experienced developers are around, sprints are also a good place for serious design discussions. Sprinters only need a table to sit around, reliable wifi, and dedication to do great things!', max_length=10),
        ),
    ]
