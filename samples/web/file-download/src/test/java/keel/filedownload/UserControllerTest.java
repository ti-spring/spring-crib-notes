package keel.filedownload;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.web.servlet.MockMvc;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest(classes = FileDownloadApplication.class)
@AutoConfigureMockMvc
@TestPropertySource("classpath:test.properties")
public class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void ファイルダウンロード画面の初期表示() throws Exception {
        mockMvc
                .perform(get("/"))
                .andExpect(status().isOk())
                .andExpect(view().name("index"));
    }

    @Test
    public void ファイルダウンロードのテスト() throws Exception {
        mockMvc
                .perform(get("/download"))
                .andExpect(status().isOk())
                .andExpect(model().hasNoErrors())
                .andExpect(content().string("test"))
                .andExpect(content().contentType("text/plain"))
                .andExpect(header().string("Content-Disposition", "attachment; filename*=UTF-8''"
                        + URLEncoder.encode("ダウンロード.txt", StandardCharsets.UTF_8)));
    }
}
