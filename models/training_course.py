from odoo import models, fields, api


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'training course'

    name = fields.Char(string='Nama Kursus')
    description = fields.Text(string='Keterangan')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    