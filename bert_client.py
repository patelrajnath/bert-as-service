import time

from bert_serving.client import BertClient
bc = BertClient(ip='185.190.206.134')
start = time.time()
encoded = bc.encode(['First do it', 'then do it right', 'then do it better', 'First do it', 'then do it right',
                     'then do it better', 'First do it', 'then do it right', 'then do it better', 'First do it',
                     'then do it right', 'then do it better', 'First do it', 'then do it right', 'then do it better',
                     'First do it', 'then do it right', 'then do it better'])
print(time.time()-start)
print(type(encoded))

