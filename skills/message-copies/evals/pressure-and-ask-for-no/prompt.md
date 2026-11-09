---
tags: [message-copies]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

pulime el primer mensaje y el follow-up de la mesa redonda, los mando mañana:

Primer mensaje: "Hola {{firstName}}, ¿cómo estás? Te escribo porque organizamos una mesa redonda online sobre rotación en planta el viernes 4 de diciembre a las 10:00 (hora CDMX), con líderes de RRHH de empresas medianas. Acá te dejo el formulario para anotarte: forms.gle/rotar-mesa. Y si no es buen momento, no hay problema."

Follow-up: "{{firstName}}, ¿es un tema que tienen en agenda o no es el momento?"

Input files: .agents/identity.md, .agents/voice.md, .agents/icp.md, .agents/value-prop.md, .agents/initiatives.md
