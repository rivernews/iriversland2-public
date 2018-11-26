# Frontend

## NPM Packages

run `npm i -D` on these packages:

```

angular2-recaptcha
tinycolor2 @types/tinycolor2

```

For other details for setting up, please see [the repo djangorest-angularcli-eb-seed](https://github.com/rivernews/djangorest-angularcli-eb-seed)

- [How do I change pushing to a different github repo?](https://help.github.com/articles/changing-a-remote-s-url/)

## Costom building Ckeditor5

[Following official doc](https://docs.ckeditor.com/ckeditor5/latest/builds/guides/development/custom-builds.html)

- cd to the right path
- clone / fork repo
- npm i
- now you can install any other npm packages you want by `npm i -D <package name>`
  - Include that new dependency in `src/ckeditor.js`
- `npm run build`

---

### Upgrading from Angular 6 to 7

- [Using this upgrade guide](https://update.angular.io/).
- For ` RxJS 6` migration part, do the following instead:
  - You can remove `rxjs-compat` from `package.json`.
  - Under `frontend/`, run `npm install rxjs-tslint`
  - Under `frontend/src`, create a file `tslint.rxJSmigration.json` which contains:

```json
{
    "rulesDirectory": [
      "../node_modules/rxjs-tslint"
    ],
    "rules": {
      "rxjs-collapse-imports": true,
      "rxjs-pipeable-operators-only": true,
      "rxjs-no-static-observable-methods": true,
      "rxjs-proper-imports": true
    },
    "jsRules": {
        "no-empty": true
    }
  }
```

  - Now back to `frontend/`, run `./node_modules/.bin/tslint -c src/tslint.rxJSmigration.json -p src/tsconfig.app.json`.
    - Will auto correct for you, but will throw ERROR when it cannot resolve the issue. Look at those error. Some of them are not true so you can just skip them. e.g. you already use `from "rxjs/operators";` to import pipes, which is the correct rxJS6 way, but it still shows ERROR about `duplicate rxjs import`.

- Do `ng update @angular/cli @angular/core`
- Before updating Angular Material, update `@angular/flex-layout` first to v7:
  - `npm uninstall -D @angular/flex-layout`
  - `npm i -D @angular/flex-layout`. This will install the latest for you instead of sticking to v6.
- You can now do `ng update @angular/material`
- Run the app. Notice there're some layout changes e.g.
  - The font size in card & chip is enlarged
  - Will shade when hover on chip.
  - ...
  - You'll want to fix them by `scss` if it's not desirable.
- That's it!

### Using Google Analytics

- [Use this angular adapter](https://github.com/angulartics/angulartics2)
- [How to write Event Tracking Info](https://developers.google.com/analytics/devguides/collection/analyticsjs/events)