{
  "targets": [
    {
      "target_name": "nantest",
      "sources": [
        "nantest.cc",
        "pi_est.cc",
        "sync.cc",
        "async.cc"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"]
    }
  ]
}
