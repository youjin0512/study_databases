### mongodb functions
- insertOne() : db.fruits.insertOne({...}) ;
- delete : db.posts.deleteMany({  }) ;
- 전체 검색 : db.fruits.find({}) ;
- projection(보여지는것) : db.posts.find({}, {_id:1, title:1, category:1, likes:1}) ;  # 숫자 1 : yes의 의미
- increase : db.posts.updateMany({}, { $inc : {likes : 1}}) ;
db.posts.find({category:"Event"}) ;
db.posts.find({}, {_id:1, title:1, category:1, likes:1}) ;
db.posts.updateMany({}) ;
db.posts.updateMany({category : "Event"}, { $inc : {likes : 100}}) ;
db.posts.find( {likes : { $eq : 2}}, {title:1, category:1, likes:1}) ;
db.posts.find( { $and : [ { category : { $in : ["Event", "Tech"] } }, { likes : { $gt : 4 } } ]}, 
							{title:1, category:1, likes:1}) ;
db.posts.updateMany({ category : {$eq : "Technology"}},
                    {$set : {likes:1, body:"update Post", date:Date()}}) ;
db.posts.updateMany({ category : {$eq : "Technology"} },
                    {$set : {new_id : 45} } ) ;

db.fruits_colors.insertOne({"name": "포도",
              "origin": "한국", 
              "price_per_kg": 8000}) ;
<!-- {
  acknowledged: true,
  insertedId: ObjectId("657bf165a8da734b4f59f458")
} -->

db.fruits_colors.insertMany
([{"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "보라색"}
 , {"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "갈색"}
 , {"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "노란색"}]);

db.fruits_colors.find( {fruits_id : { $eq : ObjectId("657bf165a8da734b4f59f458") } } ) ;

db.fruits.deleteMany({}) ;

db.fruits_colors.deleteMany({}) ;