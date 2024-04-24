from odoo import models, api, fields, tools


class CourseEnrollmentStatistics(models.Model):
    _name = 'course.enrollment.statistics'
    _auto = False

    course_id = fields.Many2one('training.course', 'Course', readonly=True)
    enroll_count = fields.Integer(string="Enroll Count", readonly=True)
    total_amount = fields.Integer('Total', readonly=True)
    discount = fields.Integer("Discount", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        # view_db = 'course_enrollment_statistics'
        q = f"""
    CREATE OR REPLACE VIEW course_enrollment_statistics AS
	(
        SELECT
			MIN(enroll.id) AS id,
        	enroll.course_id AS course_id,
        	COUNT(enroll.id) AS enroll_count,
        	SUM(enroll.total_amount) AS total_amount,
        	SUM(enroll.discount) AS discount
        FROM
        	enroll_course AS enroll 
			JOIN training_course AS course ON course.id = enroll.course_id 
		WHERE 
			course.state = 'complete'
        GROUP BY 
			enroll.course_id
	);
        """

        self.env.cr.execute(q)
