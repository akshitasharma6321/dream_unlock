import'package:flutter/material.dart';
void main()=>runApp(A());
class A extends StatelessWidget{
build(c)=>MaterialApp(
home: Scaffold(
 appBar:AppBar
(title:Text('Dream Unlock')),
body :GridView.count(
crossAxisCount:2,
 children:[
 Card(child:Center(
 child:Text('Design'))),
 Card(child:Center(
 child:Text('Commerce'))),
 Card(child:Center(
 child:Text('Medical'))),
 Card(child:Center(
 child:Text('Technology'))),
 Card(child:Center(
 child:Text('Humanities'))),
 Card(child:Center(
 child:Text('Science'))),
 ]
)
)
);
}
}
}