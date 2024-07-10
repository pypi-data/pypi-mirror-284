SELECT dh.drillhole_no                             AS dh_no,   --col
       To_char(dh.map_100000_no)
       || '-'
       || To_char(dh.dh_seq_no)                    AS unit_hyphen,           --col
       Trim(To_char(dh.obs_well_plan_code))
       || Trim(To_char(dh.obs_well_seq_no, '000')) AS obs_no,                --col
       dh.dh_name                                  AS dh_name,               --col
       summ.aq_subaq                               AS aquifer,               --col
       gdh.group_code                              AS group_code,            --col
       g.group_type_code                           AS group_type,            --col
       g.group_desc                                AS group_desc,            --col
       gdh.stand_water_level_status                AS swl_status,            --col
       gdh.swl_freq                                AS swl_freq,              --col
       gdh.salinity_status                         AS tds_status,            --col
       gdh.salinity_freq                           AS tds_freq,              --col
       gdh.comments                                AS dh_comments,           --col
       gdh.created_by                              AS dh_created_by,         --col
       gdh.creation_date                           AS dh_creation_date,      --col
       gdh.modified_by                             AS dh_modified_by,        --col
       gdh.modified_date                           AS dh_modified_date,      --col
       g.comments                                  AS group_comments,        --col
       g.created_by                                AS group_created_by,      --col
       g.creation_date                             AS group_creation_date,   --col
       g.modified_by                               AS group_modified_by,     --col
       g.modified_date                             AS group_modified_date,   --col
       dh.unit_no                                  AS unit_long,   --col
       dh.amg_easting                              AS easting,               --col
       dh.amg_northing                             AS northing,              --col
       dh.amg_zone                                 AS zone,                  --col
       dh.neg_lat_deg_real                         AS latitude,              --col
       dh.long_deg_real                            AS longitude              --col
FROM   dhdb.dd_dh_group_vw gdh
       JOIN dhdb.dd_group_vw g
         ON gdh.group_code = g.group_code
       JOIN dhdb.dd_drillhole_vw dh
         ON gdh.drillhole_no = dh.drillhole_no
       JOIN dhdb.dd_drillhole_summary_vw summ
         ON gdh.drillhole_no = summ.drillhole_no
WHERE  g.group_code IN {GROUP_CODE} --arg GROUP_CODE (sequence of str): sequence of drillhole group/obs network group codes e.g. ['ANGBRM', 'EMLR']
AND dh.deletion_ind = 'N'