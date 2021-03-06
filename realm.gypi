{
  "variables": {
    "realm_enable_sync%": "1",
    "realm_download_binaries%": "1",
    "use_realm_debug%": "<!(node -p \"'REALMJS_USE_DEBUG_CORE' in process.env ? 1 : 0\")",
    "realm_js_dir%": "<(module_root_dir)",
    "runtime%": "node"
  },
  "conditions": [
    ["use_realm_debug", {
      "variables": {
        "debug_library_suffix": "-dbg",
        "build_directory": "build.debug",
      }
    }, {
      "variables": {
        "debug_library_suffix": "",
        "build_directory": "build.release",
      }
    }]
  ],
  "targets": [
    {
      "target_name": "object-store",
      "type": "static_library",
      "include_dirs": [
        "src/object-store/src",
        "src/object-store/external/json"
      ],
      "defines": [ "REALM_PLATFORM_NODE=1" ],
      "sources": [
        "src/object-store/src/binding_callback_thread_observer.cpp",
        "src/object-store/src/collection_notifications.cpp",
        "src/object-store/src/index_set.cpp",
        "src/object-store/src/list.cpp",
        "src/object-store/src/object.cpp",
        "src/object-store/src/object_schema.cpp",
        "src/object-store/src/object_store.cpp",
        "src/object-store/src/placeholder.cpp",
        "src/object-store/src/results.cpp",
        "src/object-store/src/schema.cpp",
        "src/object-store/src/shared_realm.cpp",
        "src/object-store/src/thread_safe_reference.cpp",
        "src/object-store/src/impl/collection_change_builder.cpp",
        "src/object-store/src/impl/collection_notifier.cpp",
        "src/object-store/src/impl/list_notifier.cpp",
        "src/object-store/src/impl/object_notifier.cpp",
        "src/object-store/src/impl/primitive_list_notifier.cpp",
        "src/object-store/src/impl/realm_coordinator.cpp",
        "src/object-store/src/impl/results_notifier.cpp",
        "src/object-store/src/impl/transact_log_handler.cpp",
        "src/object-store/src/impl/weak_realm_notifier.cpp",
        "src/object-store/src/util/uuid.cpp",

        "src/object-store/external/json/json.hpp",
        "src/object-store/src/audit.hpp",
        "src/object-store/src/binding_callback_thread_observer.hpp",
        "src/object-store/src/binding_context.hpp",
        "src/object-store/src/collection_notifications.hpp",
        "src/object-store/src/execution_context_id.hpp",
        "src/object-store/src/feature_checks.hpp",
        "src/object-store/src/index_set.hpp",
        "src/object-store/src/list.hpp",
        "src/object-store/src/object.hpp",
        "src/object-store/src/object_accessor.hpp",
        "src/object-store/src/object_schema.hpp",
        "src/object-store/src/object_store.hpp",
        "src/object-store/src/property.hpp",
        "src/object-store/src/results.hpp",
        "src/object-store/src/schema.hpp",
        "src/object-store/src/shared_realm.hpp",
        "src/object-store/src/thread_safe_reference.hpp",
        "src/object-store/src/impl/collection_change_builder.hpp",
        "src/object-store/src/impl/collection_notifier.hpp",
        "src/object-store/src/impl/list_notifier.hpp",
        "src/object-store/src/impl/notification_wrapper.hpp",
        "src/object-store/src/impl/object_accessor_impl.hpp",
        "src/object-store/src/impl/object_notifier.hpp",
        "src/object-store/src/impl/primitive_list_notifier.hpp",
        "src/object-store/src/impl/realm_coordinator.hpp",
        "src/object-store/src/impl/results_notifier.hpp",
        "src/object-store/src/impl/transact_log_handler.hpp",
        "src/object-store/src/impl/weak_realm_notifier.hpp",
        "src/object-store/src/impl/apple/external_commit_helper.hpp",
        "src/object-store/src/impl/apple/keychain_helper.hpp",
        "src/object-store/src/impl/epoll/external_commit_helper.hpp",
        "src/object-store/src/impl/external_commit_helper.hpp",
        "src/object-store/src/impl/generic/external_commit_helper.hpp",
        "src/object-store/src/impl/windows/external_commit_helper.hpp",
        "src/object-store/src/sync/async_open_task.hpp",
        "src/object-store/src/sync/partial_sync.hpp",
        "src/object-store/src/sync/subscription_state.hpp",
        "src/object-store/src/sync/sync_config.hpp",
        "src/object-store/src/sync/sync_manager.hpp",
        "src/object-store/src/sync/sync_permission.hpp",
        "src/object-store/src/sync/sync_session.hpp",
        "src/object-store/src/sync/sync_user.hpp",
        "src/object-store/src/sync/impl/apple/network_reachability_observer.hpp",
        "src/object-store/src/sync/impl/apple/system_configuration.hpp",
        "src/object-store/src/sync/impl/network_reachability.hpp",
        "src/object-store/src/sync/impl/sync_client.hpp",
        "src/object-store/src/sync/impl/sync_file.hpp",
        "src/object-store/src/sync/impl/sync_metadata.hpp",
        "src/object-store/src/sync/impl/work_queue.hpp",
        "src/object-store/src/server/adapter.hpp",
        "src/object-store/src/server/admin_realm.hpp",
        "src/object-store/src/server/global_notifier.hpp",
        "src/object-store/src/util/aligned_union.hpp",
        "src/object-store/src/util/atomic_shared_ptr.hpp",
        "src/object-store/src/util/event_loop_dispatcher.hpp",
        "src/object-store/src/util/event_loop_signal.hpp",
        "src/object-store/src/util/tagged_bool.hpp",
        "src/object-store/src/util/uuid.hpp",
        "src/object-store/src/util/android/event_loop_signal.hpp",
        "src/object-store/src/util/apple/event_loop_signal.hpp",
        "src/object-store/src/util/generic/event_loop_signal.hpp",
        "src/object-store/src/util/uv/event_loop_signal.hpp",
      ],
      "conditions": [
        ["OS=='win'", {
          "sources": [
            "src/object-store/src/impl/windows/external_commit_helper.cpp",
          ]
        }],
        ["OS=='linux'", {
          "sources": [
            "src/object-store/src/impl/epoll/external_commit_helper.cpp",
          ]
        }],
        ["OS=='mac'", {
          "sources": [
            "src/object-store/src/impl/apple/external_commit_helper.cpp",
            "src/object-store/src/impl/apple/keychain_helper.cpp",
            "src/object-store/src/sync/impl/apple/network_reachability_observer.cpp",
            "src/object-store/src/sync/impl/apple/system_configuration.cpp",
          ]
        }],
        ["realm_enable_sync", {
          "dependencies": [ "realm-sync" ],
          "sources": [
            "src/object-store/src/server/adapter.cpp",
            "src/object-store/src/server/admin_realm.cpp",
            "src/object-store/src/server/global_notifier.cpp",
            "src/object-store/src/sync/impl/sync_file.cpp",
            "src/object-store/src/sync/impl/sync_metadata.cpp",
            "src/object-store/src/sync/impl/work_queue.cpp",
            "src/object-store/src/sync/partial_sync.cpp",
            "src/object-store/src/sync/async_open_task.cpp",
            "src/object-store/src/sync/sync_config.cpp",
            "src/object-store/src/sync/sync_config.cpp",
            "src/object-store/src/sync/sync_manager.cpp",
            "src/object-store/src/sync/sync_session.cpp",
            "src/object-store/src/sync/sync_user.cpp",
          ],
        }, {
          "dependencies": [ "realm-core" ]
        }]
      ],
      "all_dependent_settings": {
        "defines": [ "REALM_PLATFORM_NODE=1" ],
        "include_dirs": [
          "src/object-store/src",
          "src/object-store/src/impl/apple",
        ]
      },
      "export_dependent_settings": [
        "<@(_dependencies)" # re-export settings related to linking the realm binaries
      ]
    },
    {
      "target_name": "realm-core",
      "type": "none",
      "direct_dependent_settings": {
        "conditions": [
          ["use_realm_debug", {
            "defines": [ "REALM_DEBUG=1" ]
          }]
        ]
      },
      "link_settings": {
        "libraries": [ "-lrealm-parser<(debug_library_suffix)", "-lrealm<(debug_library_suffix)" ],
      },
      "variables": {
        "prefix": "<!(node -p \"process.env.REALM_CORE_PREFIX || String()\")"
      },
      "conditions": [
        ["prefix!=''", {
          "all_dependent_settings": {
            "include_dirs": [ "<(prefix)/src", "<(prefix)/<(build_directory)/src" ],
          },
          "link_settings": {
            "library_dirs": [ "<(prefix)/<(build_directory)/src/realm" ]
          }
        }, {
          "dependencies": [ "vendored-realm" ]
        }]
      ]
    },
    {
      "target_name": "realm-sync",
      "type": "none",
      "dependencies": [ "realm-core" ],
      "link_settings": {
          "libraries": [ "-lrealm-sync<(debug_library_suffix)" ],
          "conditions": [
              ["OS=='win'", {
                "conditions": [
                  ["target_arch=='ia32'", {
                    "libraries": [ "C:\\Program Files (x86)\\Windows Kits\\8.1\\Lib\\winv6.3\\um\\x86\\mincore.lib" ]
                  }, {
                    "libraries": [ "C:\\Program Files (x86)\\Windows Kits\\8.1\\Lib\\winv6.3\\um\\x64\\mincore.lib" ]
                  }]
                ]
              }]
          ]
      },
      "all_dependent_settings": {
        "defines": [ "REALM_ENABLE_SYNC=1" ]
      },
      "export_dependent_settings": [ "<@(_dependencies)" ], # depending on sync is tantamount to depending on core
      "variables": {
        "prefix": "<!(node -p \"process.env.REALM_SYNC_PREFIX || String()\")"
      },
      "conditions": [
        ["prefix!=''", {
          "all_dependent_settings": {
            "include_dirs": [ "<(prefix)/src", "<(prefix)/<(build_directory)/src" ],
          },
          "link_settings": {
            "library_dirs": [ "<(prefix)/<(build_directory)/src/realm" ]
          }
        }, {
          "dependencies": [ "vendored-realm" ]
        }]
      ],
    },
    {
      "target_name": "OpenSSL",
      "type": "none",
      "link_settings": {
        "conditions": [
          ["OS=='win'", {
            "conditions": [
              ["target_arch=='ia32'", {
                "libraries": [ "C:\\src\\vcpkg\\installed\\x86-windows-static\\lib\\libeay32.lib", "C:\\src\\vcpkg\\installed\\x86-windows-static\\lib\\ssleay32.lib" ]
              }, {
                "libraries": [ "C:\\src\\vcpkg\\installed\\x64-windows-static\\lib\\libeay32.lib", "C:\\src\\vcpkg\\installed\\x64-windows-static\\lib\\ssleay32.lib" ]
              }],
            ]
          }],
          ["OS=='linux'", {
            "libraries": [ "-l:libssl.a", "-l:libcrypto.a" ],
            "library_dirs": [ "/usr/lib", "/usr/lib64" ],
          }]
        ]
      }
    },
    {
      "variables": {
        "vendor_dir": "<(realm_js_dir)/vendor/realm-<(OS)-<(target_arch)<(debug_library_suffix)"
      },
      "target_name": "vendored-realm",
      "type": "none",
      "all_dependent_settings": {
        "include_dirs": [ "<(vendor_dir)/include" ],
        "library_dirs": [
          "<(vendor_dir)/lib",
          "<(vendor_dir)/lib64",
          "<(vendor_dir)/osx"
        ]
      },
      "conditions": [
        ["use_realm_debug", {
          "variables": { "download_realm_debug_flag": "--debug" }
        }, {
          "variables": { "download_realm_debug_flag": "" }
        }],
        ["realm_enable_sync", {
          "variables": { "download_realm_sync_flag": "--sync" }
        }, {
          "variables": { "download_realm_sync_flag": "" }
        }],
        ["realm_download_binaries", {
          "actions": [
            {
              "action_name": "download-realm",
              "inputs": [ "<(realm_js_dir)/scripts/download-realm.js" ],
              "outputs": [ "<(vendor_dir)" ],
              "action": [ "node", "<(realm_js_dir)/scripts/download-realm.js", "<(OS)", ">(download_realm_debug_flag)", ">(download_realm_sync_flag)", "--arch=<(target_arch)" ]
            }
          ]
        }]
      ]
    }
  ]
}
