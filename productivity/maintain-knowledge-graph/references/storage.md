# Storage and release

Separate content classification, destination audience, and encryption. Private means specific authorized readers, not necessarily owner-only or end-to-end encrypted.

| Destination | Check before write | Save/verify |
| --- | --- | --- |
| Local directory/encrypted volume | Exact path, machine/users, cloud sync; folder name does not prove encryption. | Restrictive permissions where supported, original preservation, atomic/version-safe updates. Filesystem mode does not verify cloud ACLs. |
| ChatGPT Library | Read Library skill, resolve identity/access. | Native create/replace and version guards; persist metadata and use required links. Do not make public share links without authorization. |
| Drive/OneDrive/Dropbox | Installed provider skills/tools, inherited permissions, link sharing and intended readers. | Preserve identity and conditional versions; verify resulting access. Never make a parent folder public to share one file. |
| Private repository | Actual visibility, account, access scope, branch and workflow. | Commit only chosen private artifacts, no secrets. Later public conversion needs full-history review. |
| Public repository | All blobs, diffs, logs, releases and history are public. | Only sanitized artifacts, never master/private approvals. Verify public path/content. |
| Website/object store | Verify page AND data-asset access. Login on a page does not protect public JSON. | Use relevant hosting skill; public deployment only public-safe bytes; private deployment gates all assets. |
| Unknown/custom | Discover supported tools and inspect actual audience. | Block private upload if unverifiable; prepare sanitized candidate without publishing to an unknown target. |

A storage request is not permission to email, invite, message, or grant access to others. Apply recipient-resolution rules if explicit sharing is requested.

Bind release approval to destination, effective audience, files and digests. An existing scoped instruction can satisfy the gate; don't create approval loops. New public fields, readers, destinations or broader content require reassessment. Ask about unresolved changes after preparing the reviewable candidate.

If a user requests private content at a public location, clarify intent. Do not silently reclassify or publish. Explicit approval to disclose specific facts permits a reviewed classification update followed by a new sanitized export. A hidden UI toggle never protects embedded bytes.

Keep public release summaries free of private exclusions/identifiers. Upload an explicit file allowlist, never an entire working directory. If saving partially fails, state which outputs succeeded. Do not delete earlier files or change ACLs as compensation without authorization. For conflicts, reread and reconcile instead of dropping version guards.

Maintain a public-safe master for a public-only workflow; do not silently retain private data elsewhere. Keep mixed-workflow master and exports at separate identities/locations. Updating the private master doesn't automatically authorize republishing.
