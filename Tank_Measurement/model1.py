"C:\Program Files\JetBrains\PyCharm 2017.2.3\bin\runnerw.exe" C:\Python27\python.exe "C:\Program Files\JetBrains\PyCharm 2017.2.3\helpers\pycharm\django_manage.py" inspectdb H:/DjgLeo001/TankMeasure
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CorrectFactor(models.Model):
    shell_temp = models.FloatField(blank=True, null=True)
    shell_correct_factor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Correct_factor'


class EnimerosiDex(models.Model):
    id = id = models.AutoField
    dexameni = models.CharField('Δεξαμενη',max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    p_astm = models.CharField(max_length=1, blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    eid_b_thk = models.FloatField(blank=True, null=True)
    ogkos_thk = models.FloatField(blank=True, null=True)
    ogkos_15c = models.FloatField(blank=True, null=True)
    baros_ton = models.FloatField(blank=True, null=True)
    kub_metra = models.FloatField(blank=True, null=True)
    met_tonnoi = models.FloatField(blank=True, null=True)
    sortnumber = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Enimerosi_Dex'


class KatastasiDeksamenwnAppend(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    eid_b_thk = models.FloatField(blank=True, null=True)
    ogkos_15c = models.FloatField(blank=True, null=True)
    ogkos_thk = models.FloatField(blank=True, null=True)
    baros_ton = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    select_ch = models.NullBooleanField()
    select_ch2 = models.NullBooleanField()
    select_ch3 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Katastasi_deksamenwn_append'


class Kausima(models.Model):
    id = models.AutoField
    eidos = models.CharField(max_length=50, blank=True, null=True)
    katigoria = models.CharField(max_length=50, blank=True, null=True)
    upokatigoria = models.CharField(max_length=50, blank=True, null=True)
    solines = models.FloatField(blank=True, null=True)
    sortnumber = models.TextField(blank=True, null=True)  # This field type is a guess.
    solines_m3_15 = models.FloatField(blank=True, null=True)
    solines_m3_thk = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kausima'


class KulindrDexam(models.Model):
    id = models.IntegerField()
    code = models.CharField(max_length=50, blank=True, null=True)
    pl_orofi = models.NullBooleanField()
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    periegxomeno = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    ogkos = models.FloatField(blank=True, null=True)
    geo_ups = models.FloatField(blank=True, null=True)
    geo_diam = models.FloatField(blank=True, null=True)
    ups_thal = models.FloatField(blank=True, null=True)
    ogk_kon = models.FloatField(blank=True, null=True)
    km_m_ups = models.FloatField(db_column='km/m_ups', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ups_ekx = models.FloatField(blank=True, null=True)
    ups_kat = models.FloatField(blank=True, null=True)
    m_ups_pl = models.FloatField(blank=True, null=True)
    e_ups_tr_m = models.FloatField(blank=True, null=True)
    ups_antl = models.FloatField(blank=True, null=True)
    ups_pla = models.FloatField(blank=True, null=True)
    m_ant_pos = models.FloatField(blank=True, null=True)
    e_ups_for = models.FloatField(blank=True, null=True)
    m_eis_pos = models.FloatField(blank=True, null=True)
    the_pod = models.CharField(max_length=50, blank=True, null=True)
    bar_oro = models.FloatField(blank=True, null=True)
    per_p_kat1 = models.FloatField(blank=True, null=True)
    per_p_kat2 = models.FloatField(blank=True, null=True)
    per_p_ano1 = models.FloatField(blank=True, null=True)
    per_p_ano2 = models.FloatField(blank=True, null=True)
    d1y = models.FloatField(blank=True, null=True)
    d1x = models.FloatField(blank=True, null=True)
    d2y = models.FloatField(blank=True, null=True)
    d2x = models.FloatField(blank=True, null=True)
    d3y = models.FloatField(blank=True, null=True)
    d3x = models.FloatField(blank=True, null=True)
    d4y = models.FloatField(blank=True, null=True)
    d4x = models.FloatField(blank=True, null=True)
    d5y = models.FloatField(blank=True, null=True)
    d5x = models.FloatField(blank=True, null=True)
    d6y = models.FloatField(blank=True, null=True)
    d6x = models.FloatField(blank=True, null=True)
    d7y = models.FloatField(blank=True, null=True)
    d7x = models.FloatField(blank=True, null=True)
    d8y = models.FloatField(blank=True, null=True)
    d8x = models.FloatField(blank=True, null=True)
    d9y = models.FloatField(blank=True, null=True)
    d9x = models.FloatField(blank=True, null=True)
    d10y = models.FloatField(blank=True, null=True)
    d10x = models.FloatField(blank=True, null=True)
    d11y = models.FloatField(blank=True, null=True)
    d11x = models.FloatField(blank=True, null=True)
    d12y = models.FloatField(blank=True, null=True)
    d12x = models.FloatField(blank=True, null=True)
    monosi = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Kulindr_Dexam'


class Parameters(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    etos = models.FloatField(db_column='Etos', blank=True, null=True)  # Field name made lowercase.
    minas = models.FloatField(db_column='Minas', blank=True, null=True)  # Field name made lowercase.
    select_min = models.CharField(max_length=50, blank=True, null=True)
    select_min2 = models.CharField(max_length=50, blank=True, null=True)
    select_min3 = models.CharField(max_length=50, blank=True, null=True)
    select_mch = models.BooleanField()
    select_mch2 = models.BooleanField()
    select_mch3 = models.BooleanField()
    select_katast = models.CharField(max_length=50, blank=True, null=True)
    select_katast2 = models.CharField(max_length=50, blank=True, null=True)
    select_katast3 = models.CharField(max_length=50, blank=True, null=True)
    select_ch = models.BooleanField()
    select_ch2 = models.BooleanField()
    select_ch3 = models.BooleanField()
    shellfactor = models.BooleanField(db_column='ShellFactor')  # Field name made lowercase.
    days_allowed_same_pswd = models.SmallIntegerField(blank=True, null=True)
    def_therm_periv = models.IntegerField(blank=True, null=True)
    def_piesi_aeriou = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Parameters'


class ProtokolloKulindr(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    p_astm = models.CharField(max_length=1, blank=True, null=True)
    date_pro = models.DateTimeField(blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    ypsos_epi = models.FloatField(blank=True, null=True)
    therm_epi = models.FloatField(blank=True, null=True)
    eid_b_epi = models.FloatField(blank=True, null=True)
    pro_ugr = models.FloatField(blank=True, null=True)
    pro_pl_or = models.FloatField(blank=True, null=True)
    pro_kat_pl = models.FloatField(blank=True, null=True)
    pro_kath = models.FloatField(blank=True, null=True)
    pro_th_k = models.FloatField(blank=True, null=True)
    pro_sunt = models.FloatField(blank=True, null=True)
    pro_l15c = models.FloatField(db_column='pro_L15C', blank=True, null=True)  # Field name made lowercase.
    pro_xilgr = models.FloatField(blank=True, null=True)
    epi_ugr = models.FloatField(blank=True, null=True)
    epi_pl_or = models.FloatField(blank=True, null=True)
    epi_kat_pl = models.FloatField(blank=True, null=True)
    epi_kath = models.FloatField(blank=True, null=True)
    epi_th_k = models.FloatField(blank=True, null=True)
    epi_sunt = models.FloatField(blank=True, null=True)
    epi_l15c = models.FloatField(db_column='epi_L15C', blank=True, null=True)  # Field name made lowercase.
    epi_xilgr = models.FloatField(blank=True, null=True)
    fp_litra = models.FloatField(blank=True, null=True)
    fp_xilgr = models.FloatField(blank=True, null=True)
    therm_per_pro = models.FloatField(blank=True, null=True)
    therm_per_epi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Protokollo_Kulindr'


class ProtokolloSfair(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    date_pro = models.DateTimeField(blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    piesi_pro = models.FloatField(blank=True, null=True)
    ypsos_epi = models.FloatField(blank=True, null=True)
    therm_epi = models.FloatField(blank=True, null=True)
    eid_b_epi = models.FloatField(blank=True, null=True)
    piesi_epi = models.FloatField(blank=True, null=True)
    pro_gov_ugr = models.FloatField(blank=True, null=True)
    pro_vcf = models.FloatField(blank=True, null=True)
    pro_nsv_ugr = models.FloatField(blank=True, null=True)
    pro_aer = models.FloatField(blank=True, null=True)
    pro_ugr_vac = models.FloatField(blank=True, null=True)
    pro_ugr_air = models.FloatField(blank=True, null=True)
    pro_sunt_aer = models.FloatField(blank=True, null=True)
    pro_b_aer = models.FloatField(blank=True, null=True)
    pro_sun_vac = models.FloatField(blank=True, null=True)
    pro_sun_air = models.FloatField(blank=True, null=True)
    epi_gov_ugr = models.FloatField(blank=True, null=True)
    epi_vcf = models.FloatField(blank=True, null=True)
    epi_nsv_ugr = models.FloatField(blank=True, null=True)
    epi_aer = models.FloatField(blank=True, null=True)
    epi_ugr_vac = models.FloatField(blank=True, null=True)
    epi_ugr_air = models.FloatField(blank=True, null=True)
    epi_sunt_aer = models.FloatField(blank=True, null=True)
    epi_b_aer = models.FloatField(blank=True, null=True)
    epi_sun_vac = models.FloatField(blank=True, null=True)
    epi_sun_air = models.FloatField(blank=True, null=True)
    dia_sun_vac = models.FloatField(blank=True, null=True)
    dia_sun_air = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Protokollo_Sfair'


class SfairDexam(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    ogkos = models.FloatField(blank=True, null=True)
    a_cm = models.FloatField(blank=True, null=True)
    b_cm = models.FloatField(blank=True, null=True)
    yp_cm = models.FloatField(blank=True, null=True)
    oa_lt = models.FloatField(blank=True, null=True)
    bullets = models.BooleanField()
    ogk_kon = models.FloatField(blank=True, null=True)
    ups_kat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sfair_Dexam'


class XimikoiTypoiAeriwnProtok(models.Model):
    id = models.IntegerField()
    typos_aeriou = models.CharField(db_column='typos aeriou', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ab_aeriou = models.SmallIntegerField(blank=True, null=True)
    pososto_mole = models.FloatField(blank=True, null=True)
    pososto_wt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ximikoi_typoi_aeriwn_protok'


class XimikoiTypoiAeriwnStock(models.Model):
    id = models.IntegerField()
    eidos = models.CharField(max_length=255, blank=True, null=True)
    typos_aeriou = models.CharField(db_column='typos aeriou', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ab_aeriou = models.SmallIntegerField(blank=True, null=True)
    pososto_mole = models.FloatField(blank=True, null=True)
    pososto_wt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ximikoi_typoi_aeriwn_stock'


class XimikoiTypoiAeriwnYpol(models.Model):
    id = models.IntegerField()
    typos_aeriou = models.CharField(db_column='typos aeriou', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ab_aeriou = models.SmallIntegerField(blank=True, null=True)
    pososto_mole = models.FloatField(blank=True, null=True)
    pososto_wt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ximikoi_typoi_aeriwn_ypol'


class YpolEpimKulindr(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    p_astm = models.CharField(max_length=1, blank=True, null=True)
    date_epi = models.DateTimeField(blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    litra_fort = models.FloatField(blank=True, null=True)
    xiliogr_fort = models.FloatField(blank=True, null=True)
    eid_b_fort = models.FloatField(blank=True, null=True)
    therm_fort = models.FloatField(blank=True, null=True)
    pro_ugr = models.FloatField(blank=True, null=True)
    pro_pl_or = models.FloatField(blank=True, null=True)
    pro_kat_pl = models.FloatField(blank=True, null=True)
    pro_kath = models.FloatField(blank=True, null=True)
    pro_th_k = models.FloatField(blank=True, null=True)
    pro_sunt = models.FloatField(blank=True, null=True)
    pro_l15c = models.FloatField(db_column='pro_L15C', blank=True, null=True)  # Field name made lowercase.
    pro_xilgr = models.FloatField(blank=True, null=True)
    epi_ups = models.FloatField(blank=True, null=True)
    epi_therm = models.FloatField(blank=True, null=True)
    epi_eid_b = models.FloatField(blank=True, null=True)
    epi_ugr = models.FloatField(blank=True, null=True)
    epi_pl_or = models.FloatField(blank=True, null=True)
    epi_kat_pl = models.FloatField(blank=True, null=True)
    epi_kath = models.FloatField(blank=True, null=True)
    epi_th_k = models.FloatField(blank=True, null=True)
    epi_sunt = models.FloatField(blank=True, null=True)
    epi_litra = models.FloatField(blank=True, null=True)
    epi_xilgr = models.FloatField(blank=True, null=True)
    therm_per_pro = models.FloatField(blank=True, null=True)
    therm_per_fort = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ypol_Epim_Kulindr'


class YpolEpimSfair(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    date_epi = models.DateTimeField(blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    piesi_pro = models.FloatField(blank=True, null=True)
    m3_15c_fort = models.FloatField(db_column='m3_15C_fort', blank=True, null=True)  # Field name made lowercase.
    mtvac_fort = models.FloatField(blank=True, null=True)
    eid_b_fort = models.FloatField(blank=True, null=True)
    piesi_fort = models.FloatField(blank=True, null=True)
    therm_fort = models.FloatField(blank=True, null=True)
    pro_gov_ugr = models.FloatField(blank=True, null=True)
    pro_vcf = models.FloatField(blank=True, null=True)
    pro_nsv_ugr = models.FloatField(blank=True, null=True)
    pro_aer = models.FloatField(blank=True, null=True)
    pro_ugr_vac = models.FloatField(blank=True, null=True)
    pro_ugr_air = models.FloatField(blank=True, null=True)
    pro_sunt_aer = models.FloatField(blank=True, null=True)
    pro_b_aer = models.FloatField(blank=True, null=True)
    pro_sun_vac = models.FloatField(blank=True, null=True)
    pro_sun_air = models.FloatField(blank=True, null=True)
    epi_gov_ugr = models.FloatField(blank=True, null=True)
    epi_vcf = models.FloatField(blank=True, null=True)
    epi_nsv_ugr = models.FloatField(blank=True, null=True)
    epi_aer = models.FloatField(blank=True, null=True)
    epi_ugr_vac = models.FloatField(blank=True, null=True)
    epi_ugr_air = models.FloatField(blank=True, null=True)
    epi_sunt_aer = models.FloatField(blank=True, null=True)
    epi_b_aer = models.FloatField(blank=True, null=True)
    epi_sun_vac = models.FloatField(blank=True, null=True)
    epi_sun_air = models.FloatField(blank=True, null=True)
    dia_sun_vac = models.FloatField(blank=True, null=True)
    dia_sun_air = models.FloatField(blank=True, null=True)
    ypsos_epi = models.FloatField(blank=True, null=True)
    therm_epi = models.FloatField(blank=True, null=True)
    eid_b_epi = models.FloatField(blank=True, null=True)
    piesi_epi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ypol_Epim_Sfair'


class BulletsTable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_mm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bullets_table'


class DataKatastDex(models.Model):
    id = models.IntegerField(blank=True, null=True)
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    eid_b_thk = models.FloatField(blank=True, null=True)
    ogkos_15c = models.FloatField(blank=True, null=True)
    ogkos_thk = models.FloatField(blank=True, null=True)
    baros_ton = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_katast_dex'


class DataMiniaioDeltio(models.Model):
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    p_astm = models.CharField(max_length=1, blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    eid_b_thk = models.FloatField(blank=True, null=True)
    ogkos_15c = models.FloatField(blank=True, null=True)
    ogkos_thk = models.FloatField(blank=True, null=True)
    baros_ton = models.FloatField(blank=True, null=True)
    kub_metra = models.FloatField(blank=True, null=True)
    met_tonnoi = models.FloatField(blank=True, null=True)
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    select_mch = models.BooleanField()
    select_mch2 = models.BooleanField()
    select_mch3 = models.BooleanField()
    sortnumber = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_miniaio_deltio'


class DataMiniaioDeltio2Append(models.Model):
    dexameni = models.CharField(max_length=50, blank=True, null=True)
    eidos = models.CharField(max_length=50, blank=True, null=True)
    p_astm = models.CharField(max_length=1, blank=True, null=True)
    ypsos_pro = models.FloatField(blank=True, null=True)
    therm_pro = models.FloatField(blank=True, null=True)
    eid_b_pro = models.FloatField(blank=True, null=True)
    eid_b_thk = models.FloatField(blank=True, null=True)
    ogkos_15c = models.FloatField(blank=True, null=True)
    ogkos_thk = models.FloatField(blank=True, null=True)
    baros_ton = models.FloatField(blank=True, null=True)
    kub_metra = models.FloatField(blank=True, null=True)
    met_tonnoi = models.FloatField(blank=True, null=True)
    kat_eidos = models.CharField(max_length=50, blank=True, null=True)
    select_mch = models.BooleanField()
    select_mch2 = models.BooleanField()
    select_mch3 = models.BooleanField()
    sortnumber = models.TextField(blank=True, null=True)  # This field type is a guess.
    upokatigoria = models.CharField(max_length=50, blank=True, null=True)
    upokat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_miniaio_deltio_2_append'


class DexamAuthor(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    code_dexam = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dexam_author'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class SfStm(models.Model):
    id = models.IntegerField()
    sftt = models.FloatField(blank=True, null=True)
    sftd15 = models.FloatField(blank=True, null=True)
    sftvcf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_STM'


class Sftable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    sftprod = models.CharField(max_length=50, blank=True, null=True)
    sftpre = models.FloatField(blank=True, null=True)
    sftdens = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sftable'


class StockDexam(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_dexam'


class Users(models.Model):
    id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    auth_change = models.BooleanField()
    auth_admin = models.BooleanField()
    auth_logistirio = models.BooleanField()
    flag_locked = models.BooleanField()
    pswd_changed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

