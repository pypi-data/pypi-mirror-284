
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftXORleftANDleftSHRSHLleftADDSUBleftMULDIVREMrightNOTADD AND COLON COMMA DEF DIV EQUALS ID LPAREN MUL NOT NUMBER OR REM RETURN RPAREN SHL SHR SUB XORfunction : DEF ID LPAREN params RPAREN COLON statements RETURN expressionparams : params COMMA param\n        | param\n        | emptyparam : IDempty :statements : statements statement\n        | statementstatement : ID EQUALS expressionexpression : expression ADD expression\n        | expression SUB expression\n        | expression MUL expression\n        | expression DIV expression\n        | expression REM expression\n        | expression SHR expression\n        | expression SHL expression\n        | expression AND expression\n        | expression OR expression\n        | expression XOR expressionexpression : NOT expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : ID'
    
_lr_action_items = {'DEF':([0,],[2,]),'$end':([1,19,23,24,35,37,38,39,40,41,42,43,44,45,46,47,],[0,-23,-22,-1,-20,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'ID':([2,4,10,11,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,],[3,5,5,13,13,-8,19,19,-7,-23,-9,19,19,-22,19,19,19,19,19,19,19,19,19,19,-20,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'LPAREN':([3,16,17,21,22,25,26,27,28,29,30,31,32,33,34,],[4,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'RPAREN':([4,5,6,7,8,12,19,23,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-6,-5,9,-3,-4,-2,-23,-22,-20,47,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'COMMA':([4,5,6,7,8,12,],[-6,-5,10,-3,-4,-2,]),'COLON':([9,],[11,]),'EQUALS':([13,],[16,]),'RETURN':([14,15,18,19,20,23,35,37,38,39,40,41,42,43,44,45,46,47,],[17,-8,-7,-23,-9,-22,-20,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'NOT':([16,17,21,22,25,26,27,28,29,30,31,32,33,34,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'NUMBER':([16,17,21,22,25,26,27,28,29,30,31,32,33,34,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ADD':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,25,-22,25,-20,25,-10,-11,-12,-13,-14,25,25,25,25,25,-21,]),'SUB':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,26,-22,26,-20,26,-10,-11,-12,-13,-14,26,26,26,26,26,-21,]),'MUL':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,27,-22,27,-20,27,27,27,-12,-13,-14,27,27,27,27,27,-21,]),'DIV':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,28,-22,28,-20,28,28,28,-12,-13,-14,28,28,28,28,28,-21,]),'REM':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,29,-22,29,-20,29,29,29,-12,-13,-14,29,29,29,29,29,-21,]),'SHR':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,30,-22,30,-20,30,-10,-11,-12,-13,-14,-15,-16,30,30,30,-21,]),'SHL':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,31,-22,31,-20,31,-10,-11,-12,-13,-14,-15,-16,31,31,31,-21,]),'AND':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,32,-22,32,-20,32,-10,-11,-12,-13,-14,-15,-16,-17,32,32,-21,]),'OR':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,33,-22,33,-20,33,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'XOR':([19,20,23,24,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-23,34,-22,34,-20,34,-10,-11,-12,-13,-14,-15,-16,-17,34,-19,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,],[1,]),'params':([4,],[6,]),'param':([4,10,],[7,12,]),'empty':([4,],[8,]),'statements':([11,],[14,]),'statement':([11,14,],[15,18,]),'expression':([16,17,21,22,25,26,27,28,29,30,31,32,33,34,],[20,24,35,36,37,38,39,40,41,42,43,44,45,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function","S'",1,None,None,None),
  ('function -> DEF ID LPAREN params RPAREN COLON statements RETURN expression','function',9,'p_function','assembler.py',74),
  ('params -> params COMMA param','params',3,'p_params','assembler.py',80),
  ('params -> param','params',1,'p_params','assembler.py',81),
  ('params -> empty','params',1,'p_params','assembler.py',82),
  ('param -> ID','param',1,'p_param','assembler.py',91),
  ('empty -> <empty>','empty',0,'p_empty','assembler.py',97),
  ('statements -> statements statement','statements',2,'p_statements','assembler.py',101),
  ('statements -> statement','statements',1,'p_statements','assembler.py',102),
  ('statement -> ID EQUALS expression','statement',3,'p_statement','assembler.py',106),
  ('expression -> expression ADD expression','expression',3,'p_expression_binop','assembler.py',110),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','assembler.py',111),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','assembler.py',112),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','assembler.py',113),
  ('expression -> expression REM expression','expression',3,'p_expression_binop','assembler.py',114),
  ('expression -> expression SHR expression','expression',3,'p_expression_binop','assembler.py',115),
  ('expression -> expression SHL expression','expression',3,'p_expression_binop','assembler.py',116),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','assembler.py',117),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','assembler.py',118),
  ('expression -> expression XOR expression','expression',3,'p_expression_binop','assembler.py',119),
  ('expression -> NOT expression','expression',2,'p_expression_uniop','assembler.py',129),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','assembler.py',137),
  ('expression -> NUMBER','expression',1,'p_expression_number','assembler.py',141),
  ('expression -> ID','expression',1,'p_expression_id','assembler.py',147),
]
