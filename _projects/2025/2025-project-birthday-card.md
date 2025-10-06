---
title:          "Interactive 2D Birthday Card – OpenGL Graphics Programming"
date:           2024-10-29 00:01:00 +0800
selected:       true
pub:            "CPT205 - Computer Graphics"
pub_date:       "2024"
abstract: >-
  This junior-year computer graphics course project involved creating an interactive 2D animated birthday card using C++ and OpenGL. The project demonstrates fundamental computer graphics concepts including 2D transformations, animation techniques, custom shape rendering, and user interaction handling.


  Scene Design & Visual Elements – Designed a two-page birthday card featuring a cover page with animated stars and an inner page revealing a birthday cake with candles. Implemented custom drawing functions for complex shapes including stars, ribbons, cake layers, candles with flames, and decorative elements using OpenGL primitives (triangles, quads, polygons, lines).


  Animation System – Developed multiple simultaneous animations including: (1) Breathing stars effect with smooth scaling transformations on both cover and inner pages; (2) Rotating star on cake candle using continuous angle incrementation; (3) Page-sliding transition animation between cover and inner views with smooth interpolation; (4) Falling ribbons animation with wave effects and physics-based movement when triggered by user interaction.


  Interactive Features – Implemented keyboard controls for triggering different animations and view transitions. Created a custom cursor system that replaces the default mouse pointer with a graphical element. Added click-triggered ribbon falling effect that responds to mouse events with randomized ribbon properties for variety.


  Technical Implementation – Utilized OpenGL's 2D rendering pipeline with FreeGLUT library for window management. Implemented anti-aliasing for smooth edges using GL_BLEND and GL_LINE_SMOOTH. Applied geometric transformations (translation, rotation, scaling) using OpenGL matrix operations. Created modular code structure with separate functions for each visual element to ensure maintainability.


  Color Theory & Design – Applied color theory principles using a carefully selected pastel color palette to create a harmonious and festive atmosphere. Each element features custom RGB colors with subtle variations to add depth while maintaining visual cohesion.


  Animation Timing & Control – Implemented frame-based animation using glutTimerFunc for smooth, consistent animation speeds. Designed state machines to control animation phases and transitions. Used interpolation techniques for smooth movements and scaling effects.


  This project showcases proficiency in low-level graphics programming, understanding of 2D transformation mathematics, animation principles, and creative application of computer graphics fundamentals to create an engaging interactive visual experience.
cover:          /assets/images/covers/project-birthday-card.png
authors:
- Rui Sang
links:
  Report: /assets/pdfs/projects/birthday-card/CPT205_report_Sang_Rui_2251576.pdf
---

