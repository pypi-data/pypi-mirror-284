# Browse

Types:

```python
from nolita.types import ObjectiveComplete
```

Methods:

- <code title="post /browse">client.browse.<a href="./src/nolita/resources/browse.py">create</a>(\*\*<a href="src/nolita/types/browse_create_params.py">params</a>) -> <a href="./src/nolita/types/objective_complete.py">ObjectiveComplete</a></code>

# BrowserSessions

## Pages

Types:

```python
from nolita.types.browser_sessions import (
    PageRetrieveResponse,
    PageListResponse,
    PageCloseResponse,
    PageDoResponse,
    PageNewPageResponse,
    PageStepResponse,
)
```

Methods:

- <code title="get /{browserSession}/page/{pageId}">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">retrieve</a>(page_id, \*, browser_session) -> <a href="./src/nolita/types/browser_sessions/page_retrieve_response.py">PageRetrieveResponse</a></code>
- <code title="get /{browserSession}/pages">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">list</a>(browser_session) -> <a href="./src/nolita/types/browser_sessions/page_list_response.py">PageListResponse</a></code>
- <code title="get /{browserSession}/page/{pageId}/close">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">close</a>(page_id, \*, browser_session) -> <a href="./src/nolita/types/browser_sessions/page_close_response.py">PageCloseResponse</a></code>
- <code title="post /{browserSession}/page/{pageId}/do">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">do</a>(page_id, \*, browser_session, \*\*<a href="src/nolita/types/browser_sessions/page_do_params.py">params</a>) -> <a href="./src/nolita/types/browser_sessions/page_do_response.py">PageDoResponse</a></code>
- <code title="get /{browserSession}/page/newPage">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">new_page</a>(browser_session) -> <a href="./src/nolita/types/browser_sessions/page_new_page_response.py">PageNewPageResponse</a></code>
- <code title="post /{browserSession}/page/{pageId}/step">client.browser_sessions.pages.<a href="./src/nolita/resources/browser_sessions/pages/pages.py">step</a>(page_id, \*, browser_session, \*\*<a href="src/nolita/types/browser_sessions/page_step_params.py">params</a>) -> <a href="./src/nolita/types/browser_sessions/page_step_response.py">PageStepResponse</a></code>

### Screenshots

Types:

```python
from nolita.types.browser_sessions.pages import ScreenshotRetrieveResponse
```

Methods:

- <code title="get /{browserSession}/page/{pageId}/screenshot/{type}">client.browser_sessions.pages.screenshots.<a href="./src/nolita/resources/browser_sessions/pages/screenshots.py">retrieve</a>(type, \*, browser_session, page_id) -> <a href="./src/nolita/types/browser_sessions/pages/screenshot_retrieve_response.py">ScreenshotRetrieveResponse</a></code>

### Contents

Types:

```python
from nolita.types.browser_sessions.pages import ContentRetrieveResponse
```

Methods:

- <code title="get /{browserSession}/page/{pageId}/content/{type}">client.browser_sessions.pages.contents.<a href="./src/nolita/resources/browser_sessions/pages/contents.py">retrieve</a>(type, \*, browser_session, page_id) -> <a href="./src/nolita/types/browser_sessions/pages/content_retrieve_response.py">ContentRetrieveResponse</a></code>

# BrowserSession

Types:

```python
from nolita.types import BrowserSessionCloseResponse
```

Methods:

- <code title="get /browser/{browserSession}/close">client.browser_session.<a href="./src/nolita/resources/browser_session/browser_session.py">close</a>(browser_session) -> <a href="./src/nolita/types/browser_session_close_response.py">BrowserSessionCloseResponse</a></code>

## Page

Types:

```python
from nolita.types.browser_session import PageBrowseResponse, PageGotoResponse
```

Methods:

- <code title="post /{browserSession}/page/{pageId}/browse">client.browser_session.page.<a href="./src/nolita/resources/browser_session/page.py">browse</a>(page_id, \*, browser_session, \*\*<a href="src/nolita/types/browser_session/page_browse_params.py">params</a>) -> <a href="./src/nolita/types/browser_session/page_browse_response.py">object</a></code>
- <code title="post /{browserSession}/page/{pageId}/goto">client.browser_session.page.<a href="./src/nolita/resources/browser_session/page.py">goto</a>(page_id, \*, browser_session, \*\*<a href="src/nolita/types/browser_session/page_goto_params.py">params</a>) -> <a href="./src/nolita/types/browser_session/page_goto_response.py">PageGotoResponse</a></code>

# Browser

## Session

Types:

```python
from nolita.types.browser import SessionLaunchResponse
```

Methods:

- <code title="post /browser/session/launch">client.browser.session.<a href="./src/nolita/resources/browser/session.py">launch</a>(\*\*<a href="src/nolita/types/browser/session_launch_params.py">params</a>) -> <a href="./src/nolita/types/browser/session_launch_response.py">SessionLaunchResponse</a></code>
