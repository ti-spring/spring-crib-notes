package keel.aws.s3;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.io.ResourceLoader;
import org.springframework.core.io.WritableResource;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.io.InputStream;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;

// download-start
@Service
public class AwsS3DownloadService {

    private final Logger logger = LoggerFactory.getLogger(AwsS3DownloadService.class);

    private final ResourceLoader resourceLoader;

    private final AwsS3Properties properties;

    public AwsS3DownloadService(ResourceLoader resourceLoader, AwsS3Properties properties) {
        this.resourceLoader = resourceLoader;
        this.properties = properties;
    }

    public void downloadFile(Path path) {
        Path downloadPath = Path.of("download-" + path.getFileName());
        logger.info("アップロードされた{}をダウンロードし、{}に保存します。", path.getFileName(), downloadPath.getFileName());

        if (Files.exists(downloadPath)) {
            logger.info("既に{}が存在するためファイルの保存をスキップします。", downloadPath.getFileName());
            return;
        }

        WritableResource writableResource = (WritableResource) resourceLoader.getResource(createObjectLocation(path));
        try (InputStream inputStream = writableResource.getInputStream()) {
            Files.copy(inputStream, downloadPath);

            logger.info("ファイルの保存に成功しました。");
        } catch (IOException e) {
            throw new UncheckedIOException("S3からのファイルダウンロードに失敗しました。", e);
        }
    }

    private String createObjectLocation(Path path) {
        return "s3://" + properties.getBucketName() + "/upload/" + path.getFileName();
    }
}
// download-end
