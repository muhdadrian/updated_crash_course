# Monitoring API Rate Limits

# Most APIs have rate limits, which means there’s a limit to how many requests you can make in a certain amount of time. To see if you’re approaching GitHub’s limits, enter http s://api.github.com/rate_limit into a web browser. You should see a response that begins like this:

{
    "resources": {
    --snip--
    "search": { #1
    "limit": 10, #2
    "remaining": 9, #3
    "reset": 1652338832, #4
    "used": 1,
    "resource": "search"
},
--snip--

# The information we’re interested in is the rate limit for the search API ❶. We see that the limit is 10 requests per minute ❷ and that we have 9 requests remaining for the current minute ❸. The value associated with the key "reset" represents the time in Unix or epoch time (the number of seconds since midnight on January 1, 1970) when our quota will reset ❹. If you reach your quota, you’ll get a short response that lets you know you’ve reached the API limit. If you reach the limit, just wait until your quota resets.

# Many APIs require you to register and obtain an API key or access token to make API calls. As of this writing, GitHub has no such requirement, but if you obtain an access token, your limits will be much higher.
