from django.db import models
from django.utils.crypto import get_random_string



# Create your models here.

class formModel(models.Model):
    Name = models.CharField(max_length=120, blank=True)
    Age = models.IntegerField(blank=True)
    genderChoice = models.CharField(max_length=10, null=True, blank=True)
    Opno = models.IntegerField(default=0, blank=True)
    Ipno = models.IntegerField(default=0, blank=True)
    Address = models.TextField(null=True, blank=True)
    Phoneno = models.IntegerField(blank=True)
    Kureid = models.CharField(max_length=120, blank=True, null=True)
    ChiefComplaints = models.CharField(max_length=120, null=True, blank=True)
    Historyofillness = models.CharField(max_length=120, null=True, blank=True)
    PastHistory = models.CharField(max_length=150, blank=True, null=True)
    FamilyHistory = models.CharField(max_length=150, blank=True, null=True)
    ProvisionalDiagnosis = models.CharField(max_length=150, blank=True, null=True)
    Medicationhistroy = models.CharField(max_length=120, null=True, blank=True)
    Alcohol = models.BooleanField(default=False, blank=True)
    Smoking = models.BooleanField(default=False, blank=True)
    Bowel = models.BooleanField(default=False, blank=True)
    Bladder = models.BooleanField(default=False, blank=True)
    Sleep = models.BooleanField(default=False, blank=True)
    Summary = models.TextField(null=True, blank=True)
    Examinedby = models.CharField(max_length=10, null=True, blank=True)
    Verifiedby = models.CharField(max_length=10, null=True, blank=True)
    # models of section 3 begin here
    # models of General Examination
    GeneralConditions = models.CharField(max_length=120, null=True, blank=True)
    Built = models.CharField(max_length=120, null=True, blank=True)
    PulseRate = models.IntegerField(default=0)
    Systolic = models.IntegerField(default=0)
    Diastolic = models.IntegerField(default=0)
    Temperature = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)
    Palar = models.BooleanField(default=False)
    Clubbing = models.BooleanField(default=False)
    Ictreus = models.BooleanField(default=False)
    Lymphadenopathy = models.BooleanField(default=False)
    Cyanosis = models.BooleanField(default=False)
    PittingEdema = models.BooleanField(default=False)
    NeurocutaneousMarkers = models.CharField(max_length=126, null=True)
    SubcutaneousMarkers = models.BooleanField(default=False, blank=True)
    SkeletalExamination = models.CharField(max_length=126, null=True)
    # models of CNS examination
    EyeResponse = models.CharField(max_length=126, null=True)
    VerbalResponse = models.CharField(max_length=126, null=True)
    MotorResponse = models.CharField(max_length=126, null=True)
    MMSE = models.CharField(max_length=126, null=True)
    NHISscore = models.CharField(max_length=126, null=True)
    Appearance = models.CharField(max_length=126, null=True)
    Handedness = models.CharField(max_length=126, null=True)
    Orientation = models.CharField(max_length=126, null=True)
    Emotion = models.CharField(max_length=126, null=True)
    Memory = models.CharField(max_length=126, null=True)
    SpontaneosSpeech = models.CharField(max_length=126, null=True)
    # models of Cranial Nerves
    OlfactoryLeft = models.CharField(max_length=126, null=True)
    OlfactoryRight = models.CharField(max_length=126, null=True)
    # models of optic
    VisualAcuityLeft = models.CharField(max_length=126, null=True)
    VisualAcuityRight = models.CharField(max_length=126, null=True)
    ColorVisionLeft = models.CharField(max_length=126, null=True)
    ColorVisionRIght = models.CharField(max_length=126, null=True)
    FieldLeft = models.CharField(max_length=126, null=True)
    FieldRight = models.CharField(max_length=126, null=True)
    FundusLeft = models.CharField(max_length=126, null=True)
    FundusRight = models.CharField(max_length=126, null=True)
    NystagmusLeft = models.CharField(max_length=126, null=True)
    NystagmusRight = models.CharField(max_length=126, null=True)
    # models of occulomotor, abducent, trochlear
    MovemenstLeft = models.CharField(max_length=126, null=True)
    MovemenstRight = models.CharField(max_length=126, null=True)
    PupilLeft = models.CharField(max_length=120, null=True)
    PupilRight = models.CharField(max_length=120, null=True)
    Lightreflexleft = models.CharField(max_length=120, null=True)
    Lightreflexright = models.CharField(max_length=120, null=True)
    DirectLeft = models.CharField(max_length=120, null=True)
    DirectRight = models.CharField(max_length=120, null=True)
    ConsensualLeft = models.CharField(max_length=120, null=True)
    ConsensualRight = models.CharField(max_length=120, null=True)
    nystagmusleft12 = models.CharField(max_length=120, null=True)
    nystagmusright12 = models.CharField(max_length=120, null=True)
    accomodationLeft = models.CharField(max_length=120, null=True)
    accomodationRight = models.CharField(max_length=120, null=True)
    # models of trigeminal
    sensoryLeft12 = models.CharField(max_length=120, null=True)
    sensoryRight12 = models.CharField(max_length=120, null=True)
    motorLeft = models.CharField(max_length=120, null=True)
    motorRight = models.CharField(max_length=120, null=True)
    jawjerkleft = models.CharField(max_length=120, null=True)
    jawjerkright = models.CharField(max_length=120, null=True)
    comealreflexleft = models.CharField(max_length=120, null=True)
    comealreflexright = models.CharField(max_length=120, null=True)
    # models of facial nerve
    eyeclosesureleft = models.CharField(max_length=120, null=True)
    eyeclosesureright = models.CharField(max_length=120, null=True)
    facialexpressionsleft = models.CharField(max_length=120, null=True)
    facialexpressionsright = models.CharField(max_length=120, null=True)
    Comealexpressionright = models.CharField(max_length=120, null=True)
    Comealexpressionleft = models.CharField(max_length=120, null=True)
    tasteleft = models.CharField(max_length=120, null=True)
    tasteright = models.CharField(max_length=120, null=True)
    SensoryLeft = models.CharField(max_length=120, null=True)
    SensoryRight = models.CharField(max_length=120, null=True)
    # models of Vestibulocochlear Nerve
    rhombusleft = models.CharField(max_length=120, null=True)
    rhombusright = models.CharField(max_length=120, null=True)
    rinnesleft = models.CharField(max_length=120, null=True)
    rinnesright = models.CharField(max_length=120, null=True)
    webbersleft = models.CharField(max_length=120, null=True)
    webbersright = models.CharField(max_length=120, null=True)
    ABCleft = models.CharField(max_length=120, null=True)
    ABCright = models.CharField(max_length=120, null=True)
    # models of Glosopharyngeal and Vagus
    sensoryLeft1 = models.CharField(max_length=120, null=True)
    sensoryRight1 = models.CharField(max_length=120, null=True)
    motorLeft1 = models.CharField(max_length=120, null=True)
    motorRight1 = models.CharField(max_length=120, null=True)
    Gagleft = models.CharField(max_length=120, null=True)
    GagRight = models.CharField(max_length=120, null=True)
    palatalleft = models.CharField(max_length=120, null=True)
    palatalright = models.CharField(max_length=120, null=True)
    uvulaleft = models.CharField(max_length=120, null=True)
    uvularight = models.CharField(max_length=120, null=True)
    # models of Accessory Nerve
    trapeziusleft = models.CharField(max_length=120, null=True)
    trapeziusright = models.CharField(max_length=120, null=True)
    scmleft = models.CharField(max_length=120, null=True)
    scmright = models.CharField(max_length=120, null=True)
    # models of Hypoglossal Nerve
    poweroftongueleft = models.CharField(max_length=120, null=True)
    poweroftongueright = models.CharField(max_length=120, null=True)
    wastingleft = models.CharField(max_length=120, null=True)
    wastingright = models.CharField(max_length=120, null=True)
    protrusionleft = models.CharField(max_length=120, null=True)
    protrusionright = models.CharField(max_length=120, null=True)

    # models of motor system
    # models of upper limb
    toneleft = models.CharField(max_length=120, null=True)
    toneright = models.CharField(max_length=120, null=True)
    bulkleft = models.CharField(max_length=120, null=True)
    bulkright = models.CharField(max_length=120, null=True)
    shoulderleft = models.CharField(max_length=120, null=True)
    shoulderright = models.CharField(max_length=120, null=True)
    abductionleft = models.CharField(max_length=120, null=True)
    abductionright = models.CharField(max_length=120, null=True)
    adductionleft = models.CharField(max_length=120, null=True)
    adductionright = models.CharField(max_length=120, null=True)
    flexionleft = models.CharField(max_length=120, null=True)
    flexionright = models.CharField(max_length=120, null=True)
    extensionleft = models.CharField(max_length=120, null=True)
    extensionright = models.CharField(max_length=120, null=True)
    # models of Elbow
    FlexionLeft12 = models.CharField(max_length=120, null=True)
    FlexionRight12 = models.CharField(max_length=120, null=True)
    ExtensionLeft12 = models.CharField(max_length=120, null=True)
    ExtensionRight12 = models.CharField(max_length=120, null=True)
    # models of wrist
    flexionleft1 = models.CharField(max_length=120, null=True)
    flexionright1 = models.CharField(max_length=120, null=True)
    extensionleft1 = models.CharField(max_length=120, null=True)
    extensionright1 = models.CharField(max_length=120, null=True)
    # model of hanggrip
    HangGripleft = models.CharField(max_length=120, null=True)
    HangGripright = models.CharField(max_length=120, null=True)
    # models of Lower Limb
    toneleft1 = models.CharField(max_length=120, null=True)
    toneright1 = models.CharField(max_length=120, null=True)
    BulkLeft12 = models.CharField(max_length=120)
    BulkRight12 = models.CharField(max_length=120)
    # models of Hip
    abductionleft1 = models.CharField(max_length=120, null=True)
    abductionright1 = models.CharField(max_length=120, null=True)
    adductionleft1 = models.CharField(max_length=120, null=True)
    adductionright1 = models.CharField(max_length=120, null=True)
    flexionleft2 = models.CharField(max_length=120, null=True)
    flexionright2 = models.CharField(max_length=120, null=True)
    extensionleft2 = models.CharField(max_length=120, null=True)
    extensionright2 = models.CharField(max_length=120, null=True)
    # models of Knee
    flexionleft3 = models.CharField(max_length=120, null=True)
    flexionright3 = models.CharField(max_length=120, null=True)
    extensionleft3 = models.CharField(max_length=120, null=True)
    extensionright3 = models.CharField(max_length=120, null=True)
    # models of ankle
    flexionleft4 = models.CharField(max_length=120, null=True)
    flexionright4 = models.CharField(max_length=120, null=True)
    extensionleft4 = models.CharField(max_length=120, null=True)
    extensionright4 = models.CharField(max_length=120, null=True)
    inversionleft = models.CharField(max_length=120, null=True)
    inversionright = models.CharField(max_length=120, null=True)
    eversionleft = models.CharField(max_length=120, null=True)
    eversionright = models.CharField(max_length=120, null=True)
    ehlleft = models.CharField(max_length=120, null=True)
    ehlright = models.CharField(max_length=120, null=True)
    abornmalmovementsleft = models.CharField(max_length=120, null=True)
    abnormalmovementsright = models.CharField(max_length=120, null=True)
    # models of sensory movements
    upperlimbleft = models.CharField(max_length=120, null=True)
    upperlimbright = models.CharField(max_length=120, null=True)
    trunkleft = models.CharField(max_length=120, null=True)
    trunkright = models.CharField(max_length=120, null=True)
    lowerLimbleft = models.CharField(max_length=120, null=True)
    lowerLimbright = models.CharField(max_length=120, null=True)
    # models for temperature
    upperlimbleft1 = models.CharField(max_length=102, null=True)
    upperlimbright1 = models.CharField(max_length=120, null=True)
    trunkleft = models.CharField(max_length=120, null=True)
    trunkright = models.CharField(max_length=120, null=True)
    lowerLimbleft1 = models.CharField(max_length=120, null=True)
    lowerLimbright1 = models.CharField(max_length=120, null=True)
    # models for posterior column
    vibrationLeft = models.CharField(max_length=120, null=True)
    vibrationRight = models.CharField(max_length=120, null=True)
    JPSleft = models.CharField(max_length=120, null=True)
    JPSright = models.CharField(max_length=120, null=True)
    # models for Reflexes
    bicepsleft = models.CharField(max_length=120, null=True)
    bicepsright = models.CharField(max_length=120, null=True)
    tricepsleft = models.CharField(max_length=120, null=True)
    tricepsright = models.CharField(max_length=120, null=True)
    supinatorleft = models.CharField(max_length=120, null=True)
    supinatorright = models.CharField(max_length=120, null=True)
    Kneeleft = models.CharField(max_length=120, null=True)
    Kneeright = models.CharField(max_length=120, null=True)
    Ankleleft = models.CharField(max_length=120, null=True)
    Ankleright = models.CharField(max_length=120, null=True)
    Abdominalleft = models.CharField(max_length=120, null=True)
    Abdominalright = models.CharField(max_length=120, null=True)
    Cremastricleft = models.CharField(max_length=120, null=True)
    Cremastricright = models.CharField(max_length=120, null=True)
    BCleft = models.CharField(max_length=120, null=True)
    BCright = models.CharField(max_length=120, null=True)
    PlantarLeft = models.CharField(max_length=120, null=True)
    PlantarRight = models.CharField(max_length=120, null=True)
    HOffmansLeft = models.CharField(max_length=120, null=True)
    HOffmansRight = models.CharField(max_length=120, null=True)
    Fingerflexionleft = models.CharField(max_length=120, null=True)
    Fingerflexionright = models.CharField(max_length=120, null=True)
    pectoralLeft = models.CharField(max_length=120, null=True)
    pectoralRight = models.CharField(max_length=120, null=True)
    # models of cerebellar signs
    rombersLeft = models.CharField(max_length=120, null=True)
    rombersRight = models.CharField(max_length=120, null=True)
    fingerNoseTextleft = models.CharField(max_length=120, null=True)
    fingerNoseTextright = models.CharField(max_length=120, null=True)
    pendularKneeJerkleft = models.CharField(max_length=120, null=True)
    pendularKneeJerkright = models.CharField(max_length=120, null=True)
    kneeHelltestleft = models.CharField(max_length=120, null=True)
    kneeHelltestright = models.CharField(max_length=120, null=True)
    othersLeft = models.CharField(max_length=120, null=True)
    othersRight = models.CharField(max_length=120, null=True)
    # models for other systems
    CVS = models.CharField(max_length=120)
    Abdomen = models.CharField(max_length=120)
    RespiratorySystem = models.CharField(max_length=120)
    Section4Name = models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return self.Name
