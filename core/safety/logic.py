import hashlib 
def anon(u):
 h=hashlib.sha256(
  u.encode()
).hexdigest()
  return h[:8]
def bad(t):
  k=["spam","fake","bot"]
 return any(x in t for x in k)
def score(u):
 if bad (u.lower()):
  return {"flag":1,"trust":20}
 return{
 "flag":0,
 "trust":85,
 "id":anon(u)
}
print (score("My idea"))
print (score("spam offer"))