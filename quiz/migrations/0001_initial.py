# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'quiz_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'quiz_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sub_category', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['SubCategory'])

        # Adding model 'Quiz'
        db.create_table(u'quiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.SlugField')(max_length=60)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Category'], null=True, blank=True)),
            ('random_order', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_questions', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('answers_at_end', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exam_paper', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('single_attempt', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pass_mark', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('success_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fail_text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Quiz'])

        # Adding model 'Progress'
        db.create_table(u'quiz_progress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('score', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=1024)),
        ))
        db.send_create_signal(u'quiz', ['Progress'])

        # Adding model 'Sitting'
        db.create_table(u'quiz_sitting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Quiz'])),
            ('question_order', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=1024)),
            ('question_list', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=1024)),
            ('incorrect_questions', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=1024, blank=True)),
            ('current_score', self.gf('django.db.models.fields.IntegerField')()),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_answers', self.gf('django.db.models.fields.TextField')(default='{}', blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Sitting'])

        # Adding model 'Question'
        db.create_table(u'quiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Category'], null=True, blank=True)),
            ('sub_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.SubCategory'], null=True, blank=True)),
            ('figure', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('explanation', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Question'])

        # Adding M2M table for field quiz on 'Question'
        m2m_table_name = db.shorten_name(u'quiz_question_quiz')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'quiz.question'], null=False)),
            ('quiz', models.ForeignKey(orm[u'quiz.quiz'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'quiz_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'quiz_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'quiz_subcategory')

        # Deleting model 'Quiz'
        db.delete_table(u'quiz_quiz')

        # Deleting model 'Progress'
        db.delete_table(u'quiz_progress')

        # Deleting model 'Sitting'
        db.delete_table(u'quiz_sitting')

        # Deleting model 'Question'
        db.delete_table(u'quiz_question')

        # Removing M2M table for field quiz on 'Question'
        db.delete_table(db.shorten_name(u'quiz_question_quiz'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quiz.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'quiz.progress': {
            'Meta': {'object_name': 'Progress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '1024'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'quiz.question': {
            'Meta': {'ordering': "['category']", 'object_name': 'Question'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'explanation': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'figure': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quiz.Quiz']", 'symmetrical': 'False', 'blank': 'True'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.SubCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'quiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'answers_at_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exam_paper': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fail_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_questions': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pass_mark': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'random_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'single_attempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'success_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '60'})
        },
        u'quiz.sitting': {
            'Meta': {'object_name': 'Sitting'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current_score': ('django.db.models.fields.IntegerField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incorrect_questions': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '1024', 'blank': 'True'}),
            'question_list': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '1024'}),
            'question_order': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '1024'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Quiz']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_answers': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'blank': 'True'})
        },
        u'quiz.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_category': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quiz']