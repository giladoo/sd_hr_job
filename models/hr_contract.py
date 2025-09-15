from odoo import models, fields, api

class SdHrJobHrContract(models.Model):
    _inherit = 'hr.contract'

    def generate_and_download(self,):
        context = self.env.context
        print(f"\n 222 generate_and_download\n {context}")
        model_name = context.get('model_name', False)
        active_ids = context.get('active_ids', [])
        variable_no = context.get('variable_no', False)
        output_type = context.get('output_type', 'pdf')
        file_prefix = context.get('file_prefix', 'File')
        file_name = context.get('file_name', 'name')
        attach_docs = context.get('attach_docs', False)
        # print('\n>>>>>>>>>>>\n', model_name, active_ids, variable_no, output_type )
        return self.env['sd_hr.export'].sudo().generate_and_download(model_name, active_ids, variable_no, output_type, file_prefix,  file_name, attach_docs )

