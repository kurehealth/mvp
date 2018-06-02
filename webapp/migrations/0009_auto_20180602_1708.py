# Generated by Django 2.0.5 on 2018-06-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20180513_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='ABCleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ABCright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Abdomen',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Abdominalleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Abdominalright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Ankleleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Ankleright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Appearance',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BCleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BCright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BulkLeft12',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='BulkRight12',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='CVS',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ColorVisionLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ColorVisionRIght',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Comealexpressionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Comealexpressionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ConsensualLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ConsensualRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Cremastricleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Cremastricright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Diastolic',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='DirectLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='DirectRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Emotion',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ExtensionLeft12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ExtensionRight12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='EyeResponse',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FieldLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FieldRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Fingerflexionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Fingerflexionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FlexionLeft12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FlexionRight12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FundusLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='FundusRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='GagRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Gagleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HOffmansLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HOffmansRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Handedness',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HangGripleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='HangGripright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='JPSleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='JPSright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kneeleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kneeright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Lightreflexleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Lightreflexright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='MMSE',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Memory',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='MotorResponse',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='MovemenstLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='MovemenstRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='NHISscore',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='NeurocutaneousMarkers',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='NystagmusLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='NystagmusRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='OlfactoryLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='OlfactoryRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Orientation',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PlantarLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PlantarRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PulseRate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PupilLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='PupilRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='RespiratorySystem',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='SensoryLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='SensoryRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='SkeletalExamination',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='SpontaneosSpeech',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Systolic',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Temperature',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='VerbalResponse',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='VisualAcuityLeft',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='VisualAcuityRight',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abductionright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abnormalmovementsright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='abornmalmovementsleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='accomodationLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='accomodationRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='adductionright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bicepsleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bicepsright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bulkleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='bulkright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='comealreflexleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='comealreflexright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ehlleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ehlright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eversionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eversionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionleft4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='extensionright4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eyeclosesureleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='eyeclosesureright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='facialexpressionsleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='facialexpressionsright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='fingerNoseTextleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='fingerNoseTextright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionleft4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='flexionright4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='inversionleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='inversionright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='jawjerk',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='kneeHelltestleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='kneeHelltestright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='lowerLimbright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='motorLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='motorLeft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='motorRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='motorRight1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='nystagmusleft12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='nystagmusright12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='othersLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='othersRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='palatalleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='palatalright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pectoralLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pectoralRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pendularKneeJerkleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pendularKneeJerkright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='pl',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='poweroftongueleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='poweroftongueright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='protrusion',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rhombusleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rhombusright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rinnesleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rinnesright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='rombers',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='scmleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='scmright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='sensoryLeft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='sensoryLeft12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='sensoryRight1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='sensoryRight12',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='shoulderleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='shoulderright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='supinatorleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='supinatorright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tasteleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tasteright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='toneright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trapeziusleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trapeziusright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tricepsleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='tricepsright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkleft1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='trunkright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbleft1',
            field=models.CharField(blank=True, max_length=102, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='upperlimbright1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='uvula',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='vibrationLeft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='vibrationRight',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='wastingleft',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='wastingright',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='webbers',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
