/* Collapse "## Bonus" sections into the site's <details> accordion.
 *
 * Done from the heading at runtime rather than by wrapping every section in
 * <details markdown="1"> by hand: the markdown stays clean and diffable, and a
 * Bonus section added to any page later is collapsed without the author having
 * to remember. With JS off the section simply renders open, which is the safe
 * failure — the content is still there.
 *
 * Only h2 is matched. The one `### Bonus` (claude-code) already carries its own
 * "Show steps" accordion, and nesting one inside another reads badly.
 */
(function () {
  'use strict';

  var CALLOUT = /\b(note|tip|important|warning|aside|demo|exercise)\b/;

  function isCallout(el) {
    return el && (el.tagName === 'BLOCKQUOTE' || el.tagName === 'P') &&
           CALLOUT.test(el.className);
  }

  function isBonusLabel(el) {
    return el.tagName === 'P' && el.firstElementChild &&
           el.firstElementChild.tagName === 'STRONG' &&
           /^Bonus\b/.test(el.firstElementChild.textContent);
  }

  document.querySelectorAll('.main-content h2[id^="bonus"]').forEach(function (h2) {
    var el = h2.nextElementSibling;
    var anchor = h2;

    // A leading callout ("Finished early? Try any of these.") stays visible —
    // collapsing it would hide the very prompt to open the section.
    if (isCallout(el)) { anchor = el; el = el.nextElementSibling; }

    var body = [];
    while (el && el.tagName !== 'H1' && el.tagName !== 'H2') {
      body.push(el);
      el = el.nextElementSibling;
    }
    // A trailing rule separates sections; it belongs to the page, not inside.
    while (body.length && body[body.length - 1].tagName === 'HR') body.pop();
    if (!body.length) return;

    var n = body.filter(isBonusLabel).length;
    var details = document.createElement('details');
    details.className = 'bonus';
    var summary = document.createElement('summary');
    summary.textContent = n > 1 ? 'Show ' + n + ' bonus exercises'
                        : n === 1 ? 'Show 1 bonus exercise'
                        : 'Show the bonus material';
    details.appendChild(summary);

    anchor.parentNode.insertBefore(details, anchor.nextSibling);
    body.forEach(function (node) { details.appendChild(node); });
  });
})();
