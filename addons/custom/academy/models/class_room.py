from odoo import models, fields


class AcademyClass(models.Model):
    _name = 'academy.class'
    _inherit = 'academy.course'

    name = fields.Char(string=('name'))

    def search(self, domain, offset=0, limit=None, order=None, count=False):
        """

        :param domain: [('name' ,'=','Long')]
        :param offset:
        :param limit:
        :param order:
        :param count:
        :return:
        """
        if self.env.context('foo', False):
            domain.push([('foo', '=', True)])
            pass
        res = super(AcademyClass, self).search(domain, offset=offset, limit=limit, order=order, count=count)
        return res

    def create(self, vals_list):
        """

        :param vals_list: {'name': 'KienNV'}
        :return:
        """
        if vals_list.get('age', False):
            vals_list['age'] = 25
        return super(AcademyClass, self).create(vals_list)

    def create_student(self, course_info):
        self.env['academy.course'].create(course_info)

    def write(self, vals):
        """

        :param vals: dictionary
        :return:
        """
        return super(AcademyClass, self).write(vals)

    def update_student_info(self, new_student_info):
        # students = self.env['x.student'].search([('name', '=', 'Kien')])   #tim kiem student ten kien
        students = self.env['x.student'].browse([1, 2, 3])  # tim kiem student co id la 1 2 3
        students = self.env.ref(
            'academy.student_a')  # tim den nhung external_id nhung id duoc xac dinh san roi trong data.xml
        students.write(new_student_info)

    def name_get(self):
        res = []
        for category in self:
            res.append((category.id, " / ".join(category.parents_and_self.mapped('name'))))
        return res
