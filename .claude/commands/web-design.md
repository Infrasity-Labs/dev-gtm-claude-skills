Parse the arguments: `$ARGUMENTS`

The first word is the subcommand. Everything after it is the input.

Route to the correct skill based on the subcommand:

### Design & UI

- **`frontend-design <brief or url>`** — Invoke the `frontend-design` skill. Pass the brief or URL to get distinctive visual design direction, typography, and aesthetic guidance.
- **`site-architecture <domain or goal>`** — Invoke the `site-architecture` skill. Pass the domain or goal to plan page hierarchy, navigation, URL structure, and internal linking.
- **`web-design-guidelines <file or pattern>`** — Invoke the `web-design-guidelines` skill. Pass a file or pattern to audit UI code for accessibility, UX, and web design best practices.

If no subcommand is given or the subcommand is unrecognised, display this help:

```
Design & UI:
  /web-design frontend-design <brief or url>              Get distinctive visual design direction & typography
  /web-design site-architecture <domain or goal>          Plan page hierarchy, navigation & URL structure
  /web-design web-design-guidelines <file or pattern>     Audit UI code for accessibility & UX best practices
```
