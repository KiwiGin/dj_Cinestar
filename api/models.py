# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    detalle = models.CharField(db_column='Detalle', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Distrito'


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    detalle = models.CharField(db_column='Detalle', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genero'

class Cine(models.Model):
    id = models.AutoField(primary_key=True)
    razonsocial = models.CharField(db_column='RazonSocial', max_length=30)  # Field name made lowercase.
    salas = models.IntegerField(db_column='Salas')  # Field name made lowercase.
    iddistrito = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='idDistrito', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cine'

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(db_column='Titulo', max_length=80)  # Field name made lowercase.
    fechaestreno = models.CharField(db_column='FechaEstreno', max_length=10)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=50)  # Field name made lowercase.
    generos = models.CharField(db_column='Generos', max_length=10)  # Field name made lowercase.
    idclasificacion = models.IntegerField(db_column='idClasificacion')  # Field name made lowercase.
    idestado = models.IntegerField(db_column='idEstado')  # Field name made lowercase.
    duracion = models.CharField(db_column='Duracion', max_length=3)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reparto = models.TextField(db_column='Reparto', blank=True, null=True)  # Field name made lowercase.
    sinopsis = models.TextField(db_column='Sinopsis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pelicula'

class Cinepelicula(models.Model):
    idcine = models.ForeignKey(Cine, models.DO_NOTHING, db_column='idCine', blank=True, null=True, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idpelicula = models.ForeignKey('Pelicula', models.DO_NOTHING, db_column='idPelicula', blank=True, null=True, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    sala = models.IntegerField(db_column='Sala')  # Field name made lowercase.
    horarios = models.CharField(db_column='Horarios', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CinePelicula'
        unique_together = [['idcine', 'idpelicula']]


class Cinetarifa(models.Model):
    idcine = models.ForeignKey(Cine, models.DO_NOTHING, db_column='idCine', blank=True, null=True, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    diassemana = models.CharField(db_column='DiasSemana', primary_key=True, max_length=80)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CineTarifa'
        unique_together = [['idcine', 'diassemana']]

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING,on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING,on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING,on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING,on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
