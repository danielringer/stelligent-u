#! /usr/bin/env ruby

require 'aws-sdk'

key_id = 'arn:aws:iam::858633482938:key/8a443b4d-c7fa-4c54-ab66-9c88d8d7dd9e'

s3 = Aws::S3::EncryptionV2::Client.new(
    kms_key_id: key_id,
    key_wrap_schema: :kms_context,
    content_encryption_schema: :aes_gcm_no_padding,
    security_profile: :v2
)

file = File.basename 'secret'

s3.put_object(bucket:'ringerkms', key:'secret', body: myfile)
s3.get_object(bucket:'ringerkms', key:'secret').body.read

#write to console
File.write("decrypt", File.read(s3.get_object(bucket:'ringerkms', key:'secret').body.read) )