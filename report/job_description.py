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
        lang = self.env.context.get('lang', 'en_US')
        employees = {}
        for doc in docs:
            contract = self.env['hr.contract'].sudo().search([('employee_id', '=', doc.id), ('state', '=', 'open')], limit=1)
            employees[doc.id] = ['', '', '']
            employees[doc.id][0] = contract.name if contract else ''
            employees[doc.id][1] = (jdatejs(contract.date_start, '%Y/%m/%d')  if lang == 'fa_IR' else contract.date_start.strftime('%Y-%m-%d') ) if contract else ''
            employees[doc.id][2] = (jdatejs(contract.date_end, '%Y/%m/%d')  if lang == 'fa_IR' else contract.date_end.strftime('%Y-%m-%d') ) if contract else ''
        return {
            'doc_ids': docids,
            'docs': docs,
            'employees': employees,
        }
