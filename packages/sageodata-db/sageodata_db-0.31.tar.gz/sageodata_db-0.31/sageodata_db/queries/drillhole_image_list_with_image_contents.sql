-- This function provides an index list of available drillhole images (photographs).
-- It does include the actual images (generally JPEG or PNG files).
SELECT     dh.drillhole_no AS dh_no,     --col
           To_char(dh.map_100000_no)
                      || '-'
                      || To_char(dh.dh_seq_no) AS unit_hyphen, --col
           Trim(To_char(dh.obs_well_plan_code))
                      || Trim(To_char(dh.obs_well_seq_no, '000')) AS obs_no,            --col
           dh.dh_name                                             AS dh_name,           --col
           summ.aq_subaq                                          AS aquifer,           --col
           i.image_no                                             AS image_no,          --col
           i.image                                                AS image_contents,              --col image contents as ORDIMAGE
           i.image_thumbnail                                      AS image_thumbnail_contents,    --col image thumbnail contents as ORDIMAGE
           i.data_source_code                                     AS data_source,       --col
           i.image_order                                          AS image_order,       --col
           i.image_date                                           AS image_date,        --col
           i.photographer                                         AS photographer,      --col
           i.image_title                                          AS title,             --col
           i.project                                              AS project,           --col
           i.image_direction                                      AS direction,         --col
           i.image_file_name                                      AS original_filename, --col
           i.copied_image_file_name                               AS image_filename,    --col
           i.display_rotation                                     AS rotation,          --col
           i.comments                                             AS comments,          --col
           i.pump_test_no                                         AS pump_test_no,      --col
           i.created_by                                           AS created_by,        --col
           i.creation_date                                        AS creation_date,     --col
           i.modified_by                                          AS modified_by,       --col
           i.modified_date                                        AS modified_date,     --col
           dh.unit_no      AS unit_long, --col
           dh.amg_easting                                         AS easting,           --col
           dh.amg_northing                                        AS northing,          --col
           dh.amg_zone                                            AS zone,              --col
           dh.neg_lat_deg_real                                    AS latitude,          --col
           dh.long_deg_real                                       AS longitude          --col
FROM       dhdb.dd_drillhole_vw dh
inner join dhdb.im_image i
ON         dh.drillhole_no = i.drillhole_no
inner join dhdb.dd_drillhole_summary_vw summ
ON         summ.drillhole_no = dh.drillhole_no
WHERE      dh.drillhole_no IN {DH_NO} --arg DH_NO (sequence of int): drillhole numbers or a :class:`pandas.DataFrame` with a "dh_no" column
AND dh.deletion_ind = 'N'
ORDER BY   dh.drillhole_no,
           i.image_order