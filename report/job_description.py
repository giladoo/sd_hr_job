# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api , _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, date, timedelta
import pytz
from  jdatetimext import jdatejs
from odoo import http
from icecream import ic

class SdHrJobJobDescriptionReport(models.AbstractModel):
    _name = 'report.sd_hr_job.job_description'
    # _name = 'report.hr_employee.sd_hr_resume_en_report'
    _description = 'HR Job Description'

    @api.model
    def _get_report_values(self, docids=None, data=None):
        docs = self.env['hr.employee'].browse(docids)
        employees = {}
        for doc in docs:
            contract = self.env['hr.contract'].search([('employee_id', '=', doc.id), ('state', '=', 'open')], limit=1)
            contract_no = contract.name if contract else ''
            employees[doc.id] = contract_no
        return {
            'doc_ids': docids,
            'docs': docs,
            'employees': employees,
        }
