# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.folder


def create_default_presets(apps, schema_editor):
    Preset = apps.get_model("cmsplugin_slick", "SlickCarouselPreset")
    Breakpoint = apps.get_model("cmsplugin_slick", "SlickCarouselBreakpoint")
    BreakpointsPreset = apps.get_model("cmsplugin_slick", "SlickCarouselBreakpointsPreset")
    
    db_alias = schema_editor.connection.alias
    
    Preset.objects.using(db_alias).bulk_create([
        Preset(title='Default'),
    ])
    Breakpoint.objects.using(db_alias).bulk_create([
        Breakpoint(title='sm',breakpoint='767', slides_to_show=2, slides_to_scroll=1),
        Breakpoint(title='md',breakpoint='991', slides_to_show=3, slides_to_scroll=1),
        Breakpoint(title='lg',breakpoint='1199', slides_to_show=4, slides_to_scroll=1),
    ])
    preset = BreakpointsPreset(title='Bootstrap(Mobile First)')
    preset.save()
    preset.breakpoints.add(1, 2, 3)
    preset.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlickCarousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_slick_slickcarousel', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='Title')),
                ('classes', models.TextField(blank=True, verbose_name='CSS classes')),
            ],
            options={
                'verbose_name': 'Slick Carousel',
                'verbose_name_plural': 'Slick Carousels',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlickCarouselBreakpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='Title')),
                ('breakpoint', models.PositiveIntegerField(verbose_name='Breakpoint resolution')),
                ('slides_to_show', models.PositiveIntegerField(default=1, verbose_name='Slides to show')),
                ('slides_to_scroll', models.PositiveIntegerField(default=1, verbose_name='Slides to scroll')),
                ('dots', models.NullBooleanField(verbose_name='Dots')),
                ('arrows', models.NullBooleanField(verbose_name='Arrows')),
                ('center_mode', models.NullBooleanField(verbose_name='Center mode')),
                ('center_padding', models.CharField(blank=True, max_length=10, verbose_name='Center padding')),
                ('autoplay', models.NullBooleanField(verbose_name='Autoplay')),
                ('autoplay_speed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Autoplay speed')),
            ],
            options={
                'verbose_name': 'Slick Carousel Breakpoint',
                'verbose_name_plural': 'Slick Carousels Breakpoints',
            },
        ),
        migrations.CreateModel(
            name='SlickCarouselBreakpointsPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('breakpoints', models.ManyToManyField(blank=True, to='cmsplugin_slick.SlickCarouselBreakpoint', verbose_name='Breakpoints')),
            ],
            options={
                'verbose_name': 'Slick Carousel Breakpoint Preset',
                'verbose_name_plural': 'Slick Carousels Breakpoints Presets',
            },
        ),
        migrations.CreateModel(
            name='SlickCarouselFolderImages',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_slick_slickcarouselfolderimages', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Title')),
                ('caption', models.BooleanField(default=False, verbose_name='Add caption')),
                ('autoscale', models.BooleanField(default=True, help_text='fit the image to the size of the container', verbose_name='Use automatic scaling')),
                ('thumbnail', models.BooleanField(default=True, help_text='accelerate page load and save mobile traffic.', verbose_name='Use thumbnails')),
                ('original_link', models.BooleanField(default=True, verbose_name='Link to original image')),
                ('target_blank', models.BooleanField(default=False, verbose_name='Open link in new window')),
                ('ordered_by', models.CharField(choices=[('id', 'ID'), ('original_filename', 'Filename'), ('uploaded_at', 'Uploadet at'), ('modified_at', 'Modified at')], default='original_filename', max_length=17, verbose_name='Ordered by')),
                ('reverse_order', models.BooleanField(default=False, verbose_name='Reverse order')),
                ('classes', models.TextField(blank=True, verbose_name='CSS classes')),
                ('folder', filer.fields.folder.FilerFolderField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Folder')),
                ('thumbnail_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.ThumbnailOption', verbose_name='Thumbnail options')),
            ],
            options={
                'verbose_name': 'Carousel Folder Images',
                'verbose_name_plural': 'Carousels Folders Images',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlickCarouselPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('infinite', models.BooleanField(default=True, verbose_name='Infinite')),
                ('speed', models.PositiveIntegerField(default=300, verbose_name='Speed')),
                ('dots', models.BooleanField(default=True, verbose_name='Dots')),
                ('arrows', models.BooleanField(default=True, verbose_name='Arrows')),
                ('slides_to_show', models.PositiveIntegerField(default=1, verbose_name='Slides to show')),
                ('slides_to_scroll', models.PositiveIntegerField(default=1, verbose_name='Slides to scroll')),
                ('autoplay', models.BooleanField(default=False, verbose_name='Autoplay')),
                ('autoplay_speed', models.PositiveIntegerField(default=3000, verbose_name='Autoplay speed')),
                ('pause_on_hover', models.BooleanField(default=True, verbose_name='Pause on hover')),
                ('pause_on_dots_hover', models.BooleanField(default=True, verbose_name='Pause on dots hover')),
                ('respond_to', models.CharField(choices=[('window', 'Window'), ('slider', 'Slider'), ('min', 'Smaller of the two')], default='window', max_length=6, verbose_name='Respond to')),
                ('mobile_first', models.BooleanField(default=True, help_text='Responsive settings use mobile first calculation', verbose_name='Mobile First')),
                ('fade', models.BooleanField(default=False, verbose_name='Fade animation')),
                ('rows', models.PositiveIntegerField(default=1, verbose_name='Rows')),
                ('slides_per_row', models.PositiveIntegerField(default=1, verbose_name='Slides per row')),
                ('center_mode', models.BooleanField(default=False, verbose_name='Center mode')),
                ('center_padding', models.CharField(blank=True, max_length=10, verbose_name='Center padding')),
                ('variable_width', models.BooleanField(default=False, verbose_name='Variable Width')),
                ('adaptive_height', models.BooleanField(default=False, verbose_name='Adaptive Height')),
                ('vertical', models.BooleanField(default=False, verbose_name='Vertical')),
                ('rigth_to_left', models.BooleanField(default=False, verbose_name='Right to left')),
                ('use_theme', models.BooleanField(default=True, verbose_name='Use Slick theme')),
                ('slick_theme', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='Slick theme file')),
            ],
            options={
                'verbose_name': 'Slick Carousel Preset',
                'verbose_name_plural': 'Slick Carousels Presets',
            },
        ),
        migrations.CreateModel(
            name='SlickCarouselWrappedSlide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_slick_slickcarouselwrappedslide', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Title')),
                ('classes', models.TextField(blank=True, verbose_name='CSS classes')),
            ],
            options={
                'verbose_name': 'Wrapped Slide',
                'verbose_name_plural': 'Wrapped Slides',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='slickcarousel',
            name='breakpoints',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmsplugin_slick.SlickCarouselBreakpointsPreset', verbose_name='Breakpoints'),
        ),
        migrations.AddField(
            model_name='slickcarousel',
            name='slick_preset',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmsplugin_slick.SlickCarouselPreset', verbose_name='Preset'),
        ),
        migrations.RunPython(create_default_presets),
    ]
