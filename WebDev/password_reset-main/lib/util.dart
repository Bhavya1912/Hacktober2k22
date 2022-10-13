import 'package:flutter/material.dart';

class Util {
  static void routeToWidget(context, Widget widget) {
    Navigator.push(context, MaterialPageRoute(builder: (context) => widget));
  }
}

