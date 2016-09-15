'''
Created on Sep 12, 2016

@author: phcuong
'''

from openerp import models, fields


# Use API v9. Define new class 
class mrp_routing_workcenter_input(models.Model):
    """
    Define porperty input for a workcenter.
    """
    _name = 'mrp.routing.workcenter.input'
    _description = 'Property data input of a work center'
    
    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    workcenter_operation_id = fields.Many2one('mrp.routing.workcenter', 'Workcenter Operation Input', required=True)
    
    _sql_constraints = [
            ('code_uniq', 'unique (code, workcenter_operation_id)', "Tag input code already exists !"),
    ]
    
class mrp_routing_workcenter_ouput(models.Model):
    """
    Define porperty output for a workcenter.
    """
    _name = 'mrp.routing.workcenter.output'
    _description = 'Property data output of a work center'

    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    workcenter_operation_id = fields.Many2one('mrp.routing.workcenter', 'Workcenter Operation Out', required=True)
    
    _sql_constraints = [
            ('code_uniq', 'unique (code, workcenter_operation_id)', "Tag output code already exists !"),
    ]
    
class mrp_routing_workcenter_loss(models.Model):
    """
    Define input for compute loss in a work order
    """
    _name = 'mrp.routing.workcenter.loss'
    _description = 'Property data output of a work center'

    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    rule_loss = fields.Text('Rule')
    workcenter_operation_id = fields.Many2one('mrp.routing.workcenter', 'Workcenter Operation Loss', required=True)
    
    _sql_constraints = [
            ('code_uniq', 'unique (code, workcenter_operation_id)', "Tag loss code already exists !"),
    ]

class mrp_routing_workcenter_bol(models.Model):
    """
    Define porperty output for a workcenter.
    """
    _name = 'mrp.routing.workcenter.bol'
    _description = 'Property data output of a work center'

    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    value = fields.Float('Value')
    workcenter_operation_id = fields.Many2one('mrp.routing.workcenter', 'Workcenter Operation Bill of Loss', required=True)
    
    _sql_constraints = [
            ('code_uniq', 'unique (code, workcenter_operation_id)', "Tag bill of loss code already exists !"),
    ]
        
class mrp_routing_workcenter_assignment(models.Model):
    """
    Define the assignment for a workcenter operation.
    """
    _name = 'mrp.routing.workcenter.assignment'
    _description = 'Property data output of a work center'

    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    workcenter_operation_id = fields.Many2one('mrp.routing.workcenter', 'Workcenter Operation Assignment', required=True)
    
    _sql_constraints = [
        ('code_uniq', 'unique (code, workcenter_operation_id)', "Tag assignment code already exists !"),
    ]

    
# End of define. 
