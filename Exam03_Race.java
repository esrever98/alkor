package JavaThread;
import javafx.application.Application;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;
import javafx.stage.Stage;

public class Exam03_Race extends Application{
	@Override
	public void start(Stage primaryStage) throws Exception {
		// 일단 화면을 5 영역으로 분할
		BorderPane root = new BorderPane();

		// 화면의 크기를 설정
		root.setPrefSize(700, 500);

		FlowPane center = new FlowPane();

		// 가운데 영역에 위치할 하나의 판넬을 만들어요
	}

	public static void main(String[] args) {
		// Javafx application Thread를 생성
		// 이 Thread가 start() 호출.
		launch();
	}


}
