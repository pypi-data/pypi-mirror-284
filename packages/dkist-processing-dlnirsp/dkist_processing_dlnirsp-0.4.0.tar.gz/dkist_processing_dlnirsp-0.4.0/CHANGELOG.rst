v0.4.0 (2024-07-12)
===================

Bugfixes
--------

- Correctly mock/populate OBS_IP_START_TIME in local trial workflows that don't use Observe frames. (`#9 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/9>`__)


Misc
----

- Move to version 8.2.1 of `dkist-processing-common` which includes the publication of select private methods for documentation purposes. (`#13 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/13>`__)


v0.3.0 (2024-07-01)
===================

Misc
----

- Move to version 8.1.0 of `dkist-processing-common` which includes an upgrade to airflow 2.9.2. (`#7 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/7>`__)


v0.2.1 (2024-06-25)
===================

Misc
----

- Remove High Memory Worker requirement from `InstrumentPolarizationCalibration` task. (Should have been part of `PR #4 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/4>`__)
- Pin `twine` to non-breaking version in BitBucket pipeline

v0.2.0 (2024-06-25)
===================

Features
--------

- Greatly reduce memory requirements of `InstrumentPolarizationCalibration` task (and speed it up a little bit, too). (`#4 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/4>`__)


Misc
----

- Use `nd_left_matrix_multiply` from `dkist-processing-math` and remove the local Mixin that had this method. (`#1 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/1>`__)
- Don't initialize a `parameters` object `DlnirspLinearityTaskBase`; we don't use parameters in Linearization. (`#1 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/1>`__)
- Update for new usage of `_find_most_recent_past_value` now requiring `obs_ip_start_time` or explicit time.
- Use `asdf` codecs from `dkist-processing-common` instead of locally defined codecs (they were the same). (`#1 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/1>`__)
- Use `ParameterArmIdMixin` and `_load_param_value_from_fits` from `dkist-processing-common` (they're identical). (`#1 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/1>`__)
- Update all non-DKIST dependencies (and `dkist-processing-pac`) to current versions. (`#2 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/2>`__)
- Remove crufty "build_docs" and "upload_docs" from setup.cfg. (`#2 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/2>`__)
- Put `GroupIdMixin` on `DlnirspTaskBase` instead of using it separately for each Task class. This also helps
  soften the dependencies of the `CorrectionsMixin` on `GroupIdMixin` because now the presence of the `group_id_*` methods
  is guaranteed. (`#3 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/3>`__)
- Use pre-defined `*Tag.task_FOO()` tags and controlled `TaskName.foo` values, when available. (`#5 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/5>`__)


v0.1.1 (2024-06-12)
===================

Misc
----

- Bump `dkist-fits-specifications` to v4.3.0. We need this in DL-NIRSP so some dither-related keywords are no longer required.
  (They are only present if dithering is used). (`#6 <https://bitbucket.org/dkistdc/dkist-processing-dlnirsp/pull-requests/6>`__)


v0.1.0 (2024-06-06)
===================

- Initial release. Mostly for first release to DC stacks (i.e., not "production" quality).
