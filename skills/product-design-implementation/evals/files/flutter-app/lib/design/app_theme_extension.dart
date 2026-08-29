import 'package:flutter/material.dart';

@immutable
class AppSurfaceTheme extends ThemeExtension<AppSurfaceTheme> {
  const AppSurfaceTheme({required this.sheetRadius});

  final double sheetRadius;

  @override
  AppSurfaceTheme copyWith({double? sheetRadius}) =>
      AppSurfaceTheme(sheetRadius: sheetRadius ?? this.sheetRadius);

  @override
  AppSurfaceTheme lerp(AppSurfaceTheme? other, double t) => this;
}

