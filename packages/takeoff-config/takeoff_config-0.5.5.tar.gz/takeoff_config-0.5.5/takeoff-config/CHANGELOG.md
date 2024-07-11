# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [Unreleased]

## [0.5.5] - 2024-07-10
- add `internal_port` to `AppConfig`, default at 3005
- option to specify that a random uuid be added to each reader id. Particularly, useful in distributed system where k8s is controlling multiple versions of the takeoff containers with the same input config. To stop the readers id from colliding, the random uuid can be added to the reader id. This is done by setting the `should_add_reader_id_suffixes` to `true` in the `read_from_manifest_yaml` method of `OptionAppConfig`.

## [0.5.4] - 2024-06-28
- Increase default max prompt string bytes to 150k

## [0.5.3] - 2024-05-21
- add snowflake port into AppConfig, default at 3004

## [0.5.2] - 2024-04-05
- Prune some unused settings from AppConfig (launch bools and batching settings)

## [0.5.1] - 2024-03-19

- a minor fix for cross-platform release in github ci

## [0.5.0] - 2024-03-19

- support cross-platform release for takeoff-config package

## [0.4.0] - 2024-03-08

- First versioned release of takeoff-config, with a new release process that pushes takeoff-config to pypi alongside takeoff-client with the same version [PR 1079](https://github.com/TNBase/pantheon/pull/1079)
