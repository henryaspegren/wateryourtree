# AngularJS (Unstable)

[Bower](https://github.com/bower/bower) package for [AngularJS](http://angularjs.org/). This project _makes makes no modifications_ to the stock AngularJS build.

This branch contains the exploded [`angular-1.2.0-rc.3.zip`](http://code.angularjs.org/1.2.0-rc.3/angular-1.2.0-rc.3.zip) archive.

## Usage

To avoid conflicts with the official AngularJS bowser package, this package will remain unregistered. To use it, add the following to your Bower dependencies.

```json
{
  "dependencies" : {
    "angular" : "PatternConsulting/bower-angular#v1.2.0-rc.3"
  }
}
```

**Note that _v1.2.0-rc.3_ refers to the tag**, which corresponds to the AngularJS release. Visit the [_tags_](https://github.com/PatternConsulting/bower-angular/tags) list to see available versions, and [usage notes on Bower dependencies](https://github.com/bower/bower#usage) for details.

## Branches

There is no `master` branch; only [`stable`](https://github.com/PatternConsulting/bower-angular/tree/stable) and [`unstable`](https://github.com/PatternConsulting/bower-angular/tree/unstable) branches&mdash;which track with the respective AngularJS branches.

## Rationale

This is package is slightly duplicative with [bower-angular](https://github.com/angular/bower-angular), but intends to maintain packages for both the stable and unstable AngularJS branches.
