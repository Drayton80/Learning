--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bloqueio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bloqueio (
    nome_bloqueador character varying(255) NOT NULL,
    nome_bloqueado character varying(255) NOT NULL
);


ALTER TABLE public.bloqueio OWNER TO postgres;

--
-- Name: comentario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comentario (
    id integer NOT NULL,
    id_postagem integer NOT NULL,
    id_autor character varying(255) NOT NULL,
    data timestamp without time zone,
    texto text NOT NULL
);


ALTER TABLE public.comentario OWNER TO postgres;

--
-- Name: comentario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.comentario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comentario_id_seq OWNER TO postgres;

--
-- Name: comentario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.comentario_id_seq OWNED BY public.comentario.id;


--
-- Name: marcacao_comentario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.marcacao_comentario (
    nome_perfil character varying(255) NOT NULL,
    id_comentario integer NOT NULL
);


ALTER TABLE public.marcacao_comentario OWNER TO postgres;

--
-- Name: marcacao_postagem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.marcacao_postagem (
    nome_perfil character varying(255) NOT NULL,
    id_postagem integer NOT NULL
);


ALTER TABLE public.marcacao_postagem OWNER TO postgres;

--
-- Name: notificacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notificacao (
    id integer NOT NULL,
    data timestamp without time zone,
    tipo character varying(255) NOT NULL,
    id_perfil character varying(255) NOT NULL,
    id_seguimento_seguidor character varying(255),
    id_seguimento_seguido character varying(255),
    id_marcacao_postagem_perfil character varying(255),
    id_marcacao_postagem_idpostagem integer,
    id_marcacao_comentario_perfil character varying(255),
    id_marcacao_comentario_idcomentario integer
);


ALTER TABLE public.notificacao OWNER TO postgres;

--
-- Name: notificacao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notificacao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notificacao_id_seq OWNER TO postgres;

--
-- Name: notificacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notificacao_id_seq OWNED BY public.notificacao.id;


--
-- Name: perfil; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfil (
    nome_usuario character varying(255) NOT NULL,
    nome_real character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    biografia character varying(255) NOT NULL,
    privacidade boolean NOT NULL
);


ALTER TABLE public.perfil OWNER TO postgres;

--
-- Name: postagem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.postagem (
    id integer NOT NULL,
    data timestamp without time zone,
    texto text,
    foto bytea,
    id_autor character varying(255) NOT NULL
);


ALTER TABLE public.postagem OWNER TO postgres;

--
-- Name: postagem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.postagem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.postagem_id_seq OWNER TO postgres;

--
-- Name: postagem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.postagem_id_seq OWNED BY public.postagem.id;


--
-- Name: seguimento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.seguimento (
    "confirma‡Æo" boolean NOT NULL,
    nome_seguidor character varying(255) NOT NULL,
    nome_seguido character varying(255) NOT NULL
);


ALTER TABLE public.seguimento OWNER TO postgres;

--
-- Name: topico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.topico (
    id integer NOT NULL,
    data timestamp without time zone
);


ALTER TABLE public.topico OWNER TO postgres;

--
-- Name: topico_comentario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.topico_comentario (
    id_topico integer NOT NULL,
    id_comentario integer NOT NULL
);


ALTER TABLE public.topico_comentario OWNER TO postgres;

--
-- Name: topico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.topico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.topico_id_seq OWNER TO postgres;

--
-- Name: topico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.topico_id_seq OWNED BY public.topico.id;


--
-- Name: topico_postagem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.topico_postagem (
    id_topico integer NOT NULL,
    id_postagem integer NOT NULL
);


ALTER TABLE public.topico_postagem OWNER TO postgres;

--
-- Name: comentario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario ALTER COLUMN id SET DEFAULT nextval('public.comentario_id_seq'::regclass);


--
-- Name: notificacao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao ALTER COLUMN id SET DEFAULT nextval('public.notificacao_id_seq'::regclass);


--
-- Name: postagem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postagem ALTER COLUMN id SET DEFAULT nextval('public.postagem_id_seq'::regclass);


--
-- Name: topico id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico ALTER COLUMN id SET DEFAULT nextval('public.topico_id_seq'::regclass);


--
-- Name: bloqueio bloqueio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bloqueio
    ADD CONSTRAINT bloqueio_pkey PRIMARY KEY (nome_bloqueador, nome_bloqueado);


--
-- Name: comentario comentario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_pkey PRIMARY KEY (id);


--
-- Name: marcacao_comentario marcacao_comentario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_comentario
    ADD CONSTRAINT marcacao_comentario_pkey PRIMARY KEY (nome_perfil, id_comentario);


--
-- Name: marcacao_postagem marcacao_postagem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_postagem
    ADD CONSTRAINT marcacao_postagem_pkey PRIMARY KEY (nome_perfil, id_postagem);


--
-- Name: notificacao notificacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao
    ADD CONSTRAINT notificacao_pkey PRIMARY KEY (id);


--
-- Name: perfil perfil_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfil
    ADD CONSTRAINT perfil_pkey PRIMARY KEY (nome_usuario);


--
-- Name: postagem postagem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postagem
    ADD CONSTRAINT postagem_pkey PRIMARY KEY (id);


--
-- Name: seguimento seguimento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seguimento
    ADD CONSTRAINT seguimento_pkey PRIMARY KEY (nome_seguidor, nome_seguido);


--
-- Name: topico_comentario topico_comentario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_comentario
    ADD CONSTRAINT topico_comentario_pkey PRIMARY KEY (id_topico, id_comentario);


--
-- Name: topico topico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico
    ADD CONSTRAINT topico_pkey PRIMARY KEY (id);


--
-- Name: topico_postagem topico_postagem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_postagem
    ADD CONSTRAINT topico_postagem_pkey PRIMARY KEY (id_topico, id_postagem);


--
-- Name: bloqueio bloqueio_nome_bloqueado_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bloqueio
    ADD CONSTRAINT bloqueio_nome_bloqueado_fkey FOREIGN KEY (nome_bloqueado) REFERENCES public.perfil(nome_usuario);


--
-- Name: bloqueio bloqueio_nome_bloqueador_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bloqueio
    ADD CONSTRAINT bloqueio_nome_bloqueador_fkey FOREIGN KEY (nome_bloqueador) REFERENCES public.perfil(nome_usuario);


--
-- Name: comentario comentario_id_autor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_id_autor_fkey FOREIGN KEY (id_autor) REFERENCES public.perfil(nome_usuario);


--
-- Name: comentario comentario_id_postagem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_id_postagem_fkey FOREIGN KEY (id_postagem) REFERENCES public.postagem(id);


--
-- Name: marcacao_comentario marcacao_comentario_id_comentario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_comentario
    ADD CONSTRAINT marcacao_comentario_id_comentario_fkey FOREIGN KEY (id_comentario) REFERENCES public.comentario(id);


--
-- Name: marcacao_comentario marcacao_comentario_nome_perfil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_comentario
    ADD CONSTRAINT marcacao_comentario_nome_perfil_fkey FOREIGN KEY (nome_perfil) REFERENCES public.perfil(nome_usuario);


--
-- Name: marcacao_postagem marcacao_postagem_id_postagem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_postagem
    ADD CONSTRAINT marcacao_postagem_id_postagem_fkey FOREIGN KEY (id_postagem) REFERENCES public.postagem(id);


--
-- Name: marcacao_postagem marcacao_postagem_nome_perfil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcacao_postagem
    ADD CONSTRAINT marcacao_postagem_nome_perfil_fkey FOREIGN KEY (nome_perfil) REFERENCES public.perfil(nome_usuario);


--
-- Name: notificacao notificacao_id_marcacao_comentario_perfil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao
    ADD CONSTRAINT notificacao_id_marcacao_comentario_perfil_fkey FOREIGN KEY (id_marcacao_comentario_perfil, id_marcacao_comentario_idcomentario) REFERENCES public.marcacao_comentario(nome_perfil, id_comentario);


--
-- Name: notificacao notificacao_id_marcacao_postagem_perfil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao
    ADD CONSTRAINT notificacao_id_marcacao_postagem_perfil_fkey FOREIGN KEY (id_marcacao_postagem_perfil, id_marcacao_postagem_idpostagem) REFERENCES public.marcacao_postagem(nome_perfil, id_postagem);


--
-- Name: notificacao notificacao_id_perfil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao
    ADD CONSTRAINT notificacao_id_perfil_fkey FOREIGN KEY (id_perfil) REFERENCES public.perfil(nome_usuario);


--
-- Name: notificacao notificacao_id_seguimento_seguidor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notificacao
    ADD CONSTRAINT notificacao_id_seguimento_seguidor_fkey FOREIGN KEY (id_seguimento_seguidor, id_seguimento_seguido) REFERENCES public.seguimento(nome_seguidor, nome_seguido);


--
-- Name: postagem postagem_id_autor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.postagem
    ADD CONSTRAINT postagem_id_autor_fkey FOREIGN KEY (id_autor) REFERENCES public.perfil(nome_usuario);


--
-- Name: seguimento seguimento_nome_seguido_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seguimento
    ADD CONSTRAINT seguimento_nome_seguido_fkey FOREIGN KEY (nome_seguido) REFERENCES public.perfil(nome_usuario);


--
-- Name: seguimento seguimento_nome_seguidor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seguimento
    ADD CONSTRAINT seguimento_nome_seguidor_fkey FOREIGN KEY (nome_seguidor) REFERENCES public.perfil(nome_usuario);


--
-- Name: topico_comentario topico_comentario_id_comentario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_comentario
    ADD CONSTRAINT topico_comentario_id_comentario_fkey FOREIGN KEY (id_comentario) REFERENCES public.comentario(id);


--
-- Name: topico_comentario topico_comentario_id_topico_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_comentario
    ADD CONSTRAINT topico_comentario_id_topico_fkey FOREIGN KEY (id_topico) REFERENCES public.topico(id);


--
-- Name: topico_postagem topico_postagem_id_postagem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_postagem
    ADD CONSTRAINT topico_postagem_id_postagem_fkey FOREIGN KEY (id_postagem) REFERENCES public.postagem(id);


--
-- Name: topico_postagem topico_postagem_id_topico_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.topico_postagem
    ADD CONSTRAINT topico_postagem_id_topico_fkey FOREIGN KEY (id_topico) REFERENCES public.topico(id);


--
-- PostgreSQL database dump complete
--

