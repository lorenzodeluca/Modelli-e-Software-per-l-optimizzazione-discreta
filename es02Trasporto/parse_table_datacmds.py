
# parse_table_datacmds.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASTERISK BRACKETEDSTRING COLON COLONEQ COMMA DATA END EQ INCLUDE LBRACE LBRACKET LOAD LPAREN NAMESPACE NUM_VAL PARAM QUOTEDSTRING RBRACE RBRACKET RPAREN SEMICOLON SET STORE STRING TABLE TR WORD WORDWITHLBRACKETexpr : statements\n            | statements : statements statement\n                  | statement\n                  | statements NAMESPACE WORD LBRACE statements RBRACE\n                  | NAMESPACE WORD LBRACE statements RBRACE statement : SET WORD COLONEQ datastar SEMICOLON\n                 | SET WORDWITHLBRACKET args RBRACKET COLONEQ datastar SEMICOLON\n                 | SET WORD COLON itemstar COLONEQ datastar SEMICOLON\n                 | PARAM items COLONEQ datastar SEMICOLON\n                 | TABLE items COLONEQ datastar SEMICOLON\n                 | LOAD items SEMICOLON\n                 | STORE items SEMICOLON\n                 | INCLUDE WORD SEMICOLON\n                 | INCLUDE QUOTEDSTRING SEMICOLON\n                 | DATA SEMICOLON\n                 | END SEMICOLON\n    \n    datastar : data\n             |\n    \n    data : data NUM_VAL\n         | data WORD\n         | data STRING\n         | data QUOTEDSTRING\n         | data BRACKETEDSTRING\n         | data SET\n         | data TABLE\n         | data PARAM\n         | data LPAREN\n         | data RPAREN\n         | data COMMA\n         | data ASTERISK\n         | NUM_VAL\n         | WORD\n         | STRING\n         | QUOTEDSTRING\n         | BRACKETEDSTRING\n         | SET\n         | TABLE\n         | PARAM\n         | LPAREN\n         | RPAREN\n         | COMMA\n         | ASTERISK\n    \n    args : arg\n         |\n    \n    arg : arg COMMA NUM_VAL\n         | arg COMMA WORD\n         | arg COMMA STRING\n         | arg COMMA QUOTEDSTRING\n         | arg COMMA SET\n         | arg COMMA TABLE\n         | arg COMMA PARAM\n         | NUM_VAL\n         | WORD\n         | STRING\n         | QUOTEDSTRING\n         | SET\n         | TABLE\n         | PARAM\n    \n    itemstar : items\n             |\n    \n    items : items NUM_VAL\n          | items WORD\n          | items STRING\n          | items QUOTEDSTRING\n          | items COMMA\n          | items COLON\n          | items LBRACE\n          | items RBRACE\n          | items LBRACKET\n          | items RBRACKET\n          | items TR\n          | items LPAREN\n          | items RPAREN\n          | items ASTERISK\n          | items EQ\n          | items SET\n          | items TABLE\n          | items PARAM\n          | NUM_VAL\n          | WORD\n          | STRING\n          | QUOTEDSTRING\n          | COMMA\n          | COLON\n          | LBRACKET\n          | RBRACKET\n          | LBRACE\n          | RBRACE\n          | TR\n          | LPAREN\n          | RPAREN\n          | ASTERISK\n          | EQ\n          | SET\n          | TABLE\n          | PARAM\n    '
    
_lr_action_items = {'$end':([0,1,2,3,13,42,43,77,78,79,80,104,105,127,128,129,132,133,],[-2,0,-1,-4,-3,-16,-17,-12,-13,-14,-15,-6,-7,-10,-11,-5,-9,-8,]),'NAMESPACE':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[4,14,-4,-3,-16,-17,4,-12,-13,-14,-15,4,14,14,-6,-7,-10,-11,-5,-9,-8,]),'SET':([0,2,3,6,7,8,9,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,45,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,127,128,129,132,133,],[5,5,-4,35,35,35,35,-3,48,-97,74,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,74,74,74,-16,-17,5,83,35,-79,83,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,83,-12,-13,-14,-15,5,5,-37,-33,111,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,74,124,5,-6,-7,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,83,83,-10,-11,-5,-9,-8,]),'PARAM':([0,2,3,6,7,8,9,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,45,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,127,128,129,132,133,],[6,6,-4,18,18,18,18,-3,56,-97,57,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,57,57,57,-16,-17,6,92,18,-79,92,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,92,-12,-13,-14,-15,6,6,-37,-33,113,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,57,126,6,-6,-7,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,92,92,-10,-11,-5,-9,-8,]),'TABLE':([0,2,3,6,7,8,9,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,45,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,127,128,129,132,133,],[7,7,-4,36,36,36,36,-3,55,-97,75,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,75,75,75,-16,-17,7,91,36,-79,91,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,91,-12,-13,-14,-15,7,7,-37,-33,112,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,75,125,7,-6,-7,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,91,91,-10,-11,-5,-9,-8,]),'LOAD':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[8,8,-4,-3,-16,-17,8,-12,-13,-14,-15,8,8,8,-6,-7,-10,-11,-5,-9,-8,]),'STORE':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[9,9,-4,-3,-16,-17,9,-12,-13,-14,-15,9,9,9,-6,-7,-10,-11,-5,-9,-8,]),'INCLUDE':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[10,10,-4,-3,-16,-17,10,-12,-13,-14,-15,10,10,10,-6,-7,-10,-11,-5,-9,-8,]),'DATA':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[11,11,-4,-3,-16,-17,11,-12,-13,-14,-15,11,11,11,-6,-7,-10,-11,-5,-9,-8,]),'END':([0,2,3,13,42,43,45,77,78,79,80,81,82,103,104,105,127,128,129,132,133,],[12,12,-4,-3,-16,-17,12,-12,-13,-14,-15,12,12,12,-6,-7,-10,-11,-5,-9,-8,]),'RBRACE':([3,6,7,8,9,13,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,78,79,80,82,98,103,104,105,127,128,129,132,133,],[-4,27,27,27,27,-3,-97,66,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,66,66,66,-16,-17,27,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-12,-13,-14,-15,104,66,129,-6,-7,-10,-11,-5,-9,-8,]),'WORD':([4,5,6,7,8,9,10,14,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[15,16,21,21,21,21,40,44,52,-97,60,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,60,60,60,84,21,-79,84,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,84,-37,-33,107,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,60,121,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,84,84,]),'WORDWITHLBRACKET':([5,],[17,]),'NUM_VAL':([6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[20,20,20,20,51,-97,59,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,59,59,59,87,20,-79,87,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,87,-37,-33,106,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,59,120,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,87,87,]),'STRING':([6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[22,22,22,22,53,-97,61,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,61,61,61,88,22,-79,88,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,88,-37,-33,108,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,61,122,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,88,88,]),'QUOTEDSTRING':([6,7,8,9,10,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,100,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[23,23,23,23,41,54,-97,62,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,62,62,62,89,23,-79,89,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,89,-37,-33,109,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,62,123,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,89,89,]),'COMMA':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,],[24,24,24,24,-97,63,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,63,63,63,95,24,-57,100,-53,-54,-55,-56,-58,-59,-79,95,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,95,-37,-33,116,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,63,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,95,95,-46,-47,-48,-49,-50,-51,-52,]),'COLON':([6,7,8,9,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,],[25,25,25,25,47,-97,64,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,64,64,64,25,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,64,]),'LBRACKET':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,],[28,28,28,28,-97,67,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,67,67,67,28,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,67,]),'RBRACKET':([6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,120,121,122,123,124,125,126,],[29,29,29,29,-45,-97,68,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,68,68,68,29,-57,99,-44,-53,-54,-55,-56,-58,-59,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,68,-46,-47,-48,-49,-50,-51,-52,]),'LBRACE':([6,7,8,9,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,44,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,],[26,26,26,26,45,-97,65,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,65,65,65,81,26,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,65,]),'TR':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,],[30,30,30,30,-97,69,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,69,69,69,30,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,69,]),'LPAREN':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[31,31,31,31,-97,70,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,70,70,70,93,31,-79,93,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,93,-37,-33,114,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,70,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,93,93,]),'RPAREN':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[32,32,32,32,-97,71,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,71,71,71,94,32,-79,94,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,94,-37,-33,115,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,71,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,94,94,]),'ASTERISK':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,94,95,96,98,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[33,33,33,33,-97,72,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,72,72,72,96,33,-79,96,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,96,-37,-33,117,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,72,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,96,96,]),'EQ':([6,7,8,9,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,98,],[34,34,34,34,-97,73,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,73,73,73,34,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,73,]),'SEMICOLON':([11,12,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,46,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,83,84,85,86,87,88,89,90,91,92,93,94,95,96,101,102,106,107,108,109,110,111,112,113,114,115,116,117,118,119,130,131,],[42,43,-97,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,77,78,79,80,-19,-79,-19,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-19,-37,-33,105,-18,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,127,128,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-19,-19,132,133,]),'COLONEQ':([16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,47,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,97,98,99,],[46,-97,58,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-90,-91,-92,-93,-94,-95,-96,76,-61,-79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,118,-60,119,]),'BRACKETEDSTRING':([46,58,76,83,84,86,87,88,89,90,91,92,93,94,95,96,106,107,108,109,110,111,112,113,114,115,116,117,118,119,],[90,90,90,-37,-33,110,-32,-34,-35,-36,-38,-39,-40,-41,-42,-43,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,90,90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,],[1,]),'statements':([0,45,81,],[2,82,103,]),'statement':([0,2,45,81,82,103,],[3,13,3,3,13,13,]),'items':([6,7,8,9,47,],[19,37,38,39,98,]),'args':([17,],[49,]),'arg':([17,],[50,]),'datastar':([46,58,76,118,119,],[85,101,102,130,131,]),'data':([46,58,76,118,119,],[86,86,86,86,86,]),'itemstar':([47,],[97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> statements','expr',1,'p_expr','parse_datacmds.py',200),
  ('expr -> <empty>','expr',0,'p_expr','parse_datacmds.py',201),
  ('statements -> statements statement','statements',2,'p_statements','parse_datacmds.py',215),
  ('statements -> statement','statements',1,'p_statements','parse_datacmds.py',216),
  ('statements -> statements NAMESPACE WORD LBRACE statements RBRACE','statements',6,'p_statements','parse_datacmds.py',217),
  ('statements -> NAMESPACE WORD LBRACE statements RBRACE','statements',5,'p_statements','parse_datacmds.py',218),
  ('statement -> SET WORD COLONEQ datastar SEMICOLON','statement',5,'p_statement','parse_datacmds.py',240),
  ('statement -> SET WORDWITHLBRACKET args RBRACKET COLONEQ datastar SEMICOLON','statement',7,'p_statement','parse_datacmds.py',241),
  ('statement -> SET WORD COLON itemstar COLONEQ datastar SEMICOLON','statement',7,'p_statement','parse_datacmds.py',242),
  ('statement -> PARAM items COLONEQ datastar SEMICOLON','statement',5,'p_statement','parse_datacmds.py',243),
  ('statement -> TABLE items COLONEQ datastar SEMICOLON','statement',5,'p_statement','parse_datacmds.py',244),
  ('statement -> LOAD items SEMICOLON','statement',3,'p_statement','parse_datacmds.py',245),
  ('statement -> STORE items SEMICOLON','statement',3,'p_statement','parse_datacmds.py',246),
  ('statement -> INCLUDE WORD SEMICOLON','statement',3,'p_statement','parse_datacmds.py',247),
  ('statement -> INCLUDE QUOTEDSTRING SEMICOLON','statement',3,'p_statement','parse_datacmds.py',248),
  ('statement -> DATA SEMICOLON','statement',2,'p_statement','parse_datacmds.py',249),
  ('statement -> END SEMICOLON','statement',2,'p_statement','parse_datacmds.py',250),
  ('datastar -> data','datastar',1,'p_datastar','parse_datacmds.py',277),
  ('datastar -> <empty>','datastar',0,'p_datastar','parse_datacmds.py',278),
  ('data -> data NUM_VAL','data',2,'p_data','parse_datacmds.py',287),
  ('data -> data WORD','data',2,'p_data','parse_datacmds.py',288),
  ('data -> data STRING','data',2,'p_data','parse_datacmds.py',289),
  ('data -> data QUOTEDSTRING','data',2,'p_data','parse_datacmds.py',290),
  ('data -> data BRACKETEDSTRING','data',2,'p_data','parse_datacmds.py',291),
  ('data -> data SET','data',2,'p_data','parse_datacmds.py',292),
  ('data -> data TABLE','data',2,'p_data','parse_datacmds.py',293),
  ('data -> data PARAM','data',2,'p_data','parse_datacmds.py',294),
  ('data -> data LPAREN','data',2,'p_data','parse_datacmds.py',295),
  ('data -> data RPAREN','data',2,'p_data','parse_datacmds.py',296),
  ('data -> data COMMA','data',2,'p_data','parse_datacmds.py',297),
  ('data -> data ASTERISK','data',2,'p_data','parse_datacmds.py',298),
  ('data -> NUM_VAL','data',1,'p_data','parse_datacmds.py',299),
  ('data -> WORD','data',1,'p_data','parse_datacmds.py',300),
  ('data -> STRING','data',1,'p_data','parse_datacmds.py',301),
  ('data -> QUOTEDSTRING','data',1,'p_data','parse_datacmds.py',302),
  ('data -> BRACKETEDSTRING','data',1,'p_data','parse_datacmds.py',303),
  ('data -> SET','data',1,'p_data','parse_datacmds.py',304),
  ('data -> TABLE','data',1,'p_data','parse_datacmds.py',305),
  ('data -> PARAM','data',1,'p_data','parse_datacmds.py',306),
  ('data -> LPAREN','data',1,'p_data','parse_datacmds.py',307),
  ('data -> RPAREN','data',1,'p_data','parse_datacmds.py',308),
  ('data -> COMMA','data',1,'p_data','parse_datacmds.py',309),
  ('data -> ASTERISK','data',1,'p_data','parse_datacmds.py',310),
  ('args -> arg','args',1,'p_args','parse_datacmds.py',333),
  ('args -> <empty>','args',0,'p_args','parse_datacmds.py',334),
  ('arg -> arg COMMA NUM_VAL','arg',3,'p_arg','parse_datacmds.py',343),
  ('arg -> arg COMMA WORD','arg',3,'p_arg','parse_datacmds.py',344),
  ('arg -> arg COMMA STRING','arg',3,'p_arg','parse_datacmds.py',345),
  ('arg -> arg COMMA QUOTEDSTRING','arg',3,'p_arg','parse_datacmds.py',346),
  ('arg -> arg COMMA SET','arg',3,'p_arg','parse_datacmds.py',347),
  ('arg -> arg COMMA TABLE','arg',3,'p_arg','parse_datacmds.py',348),
  ('arg -> arg COMMA PARAM','arg',3,'p_arg','parse_datacmds.py',349),
  ('arg -> NUM_VAL','arg',1,'p_arg','parse_datacmds.py',350),
  ('arg -> WORD','arg',1,'p_arg','parse_datacmds.py',351),
  ('arg -> STRING','arg',1,'p_arg','parse_datacmds.py',352),
  ('arg -> QUOTEDSTRING','arg',1,'p_arg','parse_datacmds.py',353),
  ('arg -> SET','arg',1,'p_arg','parse_datacmds.py',354),
  ('arg -> TABLE','arg',1,'p_arg','parse_datacmds.py',355),
  ('arg -> PARAM','arg',1,'p_arg','parse_datacmds.py',356),
  ('itemstar -> items','itemstar',1,'p_itemstar','parse_datacmds.py',379),
  ('itemstar -> <empty>','itemstar',0,'p_itemstar','parse_datacmds.py',380),
  ('items -> items NUM_VAL','items',2,'p_items','parse_datacmds.py',389),
  ('items -> items WORD','items',2,'p_items','parse_datacmds.py',390),
  ('items -> items STRING','items',2,'p_items','parse_datacmds.py',391),
  ('items -> items QUOTEDSTRING','items',2,'p_items','parse_datacmds.py',392),
  ('items -> items COMMA','items',2,'p_items','parse_datacmds.py',393),
  ('items -> items COLON','items',2,'p_items','parse_datacmds.py',394),
  ('items -> items LBRACE','items',2,'p_items','parse_datacmds.py',395),
  ('items -> items RBRACE','items',2,'p_items','parse_datacmds.py',396),
  ('items -> items LBRACKET','items',2,'p_items','parse_datacmds.py',397),
  ('items -> items RBRACKET','items',2,'p_items','parse_datacmds.py',398),
  ('items -> items TR','items',2,'p_items','parse_datacmds.py',399),
  ('items -> items LPAREN','items',2,'p_items','parse_datacmds.py',400),
  ('items -> items RPAREN','items',2,'p_items','parse_datacmds.py',401),
  ('items -> items ASTERISK','items',2,'p_items','parse_datacmds.py',402),
  ('items -> items EQ','items',2,'p_items','parse_datacmds.py',403),
  ('items -> items SET','items',2,'p_items','parse_datacmds.py',404),
  ('items -> items TABLE','items',2,'p_items','parse_datacmds.py',405),
  ('items -> items PARAM','items',2,'p_items','parse_datacmds.py',406),
  ('items -> NUM_VAL','items',1,'p_items','parse_datacmds.py',407),
  ('items -> WORD','items',1,'p_items','parse_datacmds.py',408),
  ('items -> STRING','items',1,'p_items','parse_datacmds.py',409),
  ('items -> QUOTEDSTRING','items',1,'p_items','parse_datacmds.py',410),
  ('items -> COMMA','items',1,'p_items','parse_datacmds.py',411),
  ('items -> COLON','items',1,'p_items','parse_datacmds.py',412),
  ('items -> LBRACKET','items',1,'p_items','parse_datacmds.py',413),
  ('items -> RBRACKET','items',1,'p_items','parse_datacmds.py',414),
  ('items -> LBRACE','items',1,'p_items','parse_datacmds.py',415),
  ('items -> RBRACE','items',1,'p_items','parse_datacmds.py',416),
  ('items -> TR','items',1,'p_items','parse_datacmds.py',417),
  ('items -> LPAREN','items',1,'p_items','parse_datacmds.py',418),
  ('items -> RPAREN','items',1,'p_items','parse_datacmds.py',419),
  ('items -> ASTERISK','items',1,'p_items','parse_datacmds.py',420),
  ('items -> EQ','items',1,'p_items','parse_datacmds.py',421),
  ('items -> SET','items',1,'p_items','parse_datacmds.py',422),
  ('items -> TABLE','items',1,'p_items','parse_datacmds.py',423),
  ('items -> PARAM','items',1,'p_items','parse_datacmds.py',424),
]
